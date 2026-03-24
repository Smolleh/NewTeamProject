from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import createUserForm
from django.contrib.auth import login, logout, authenticate
from .permissions import isCurator
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .decorators import rate_limiter


class CuratorProtectedView(APIView):
    permission_classes = [isCurator]

#view to list all exhibit information
class UserExhibitsView(generics.ListAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = SimpleViewExhibitSerializer

#view to see a psecific exhibit, including the associated failure categories, artefacts, lessons learned, etc..
class UserSingleExhibitView(generics.RetrieveAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    
#functional view to delete the request's user's data, setting their results and comments to null and deleting all other data
@login_required
def deleteUser(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

#view for curators to view all exhibits and create new ones
class AdminExhibitsView(CuratorProtectedView, generics.ListCreateAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = SimpleViewCreateExhibitSerializer

#view for curators to update and delete specifc exhibits (and all associated entries)
class AdminEditExhibitView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
 
#view for curators to  create artefacts (with their images)
class AdminCreateArtefactView(CuratorProtectedView, generics.CreateAPIView): 
    serializer_class = ArtefactSerializer 
    def perform_create(self, serializer): 
        exhibit = get_object_or_404(Exhibit, exhibitId=self.kwargs["exhibitId"]) 
        image = self.request.FILES.get('artefactObjectPath')
        serializer.save(exhibitId=exhibit, artefactObjectPath=image) 
        
#curator view for editing or deleting artefacts 
class AdminEditArtefactView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = ArtefactSerializer 
    def get_queryset(self): 
        return Artefact.objects.filter(exhibitId=self.kwargs["exhibitId"])
    
    

#curator view to edit or delete an AI system description
class AdminEditSystemDescView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AiSystemDescriptionSerializer

    def get_object(self):
        
        return get_object_or_404(AiSystemDescription, exhibitId=self.kwargs["exhibitId"])
    
#curator view to edit or delete lessons learned
class AdminEditLessonsLearnedView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonsLearnedSerializer

    def get_object(self):

        return get_object_or_404(LessonsLearned, exhibitId=self.kwargs["exhibitId"])

#curator view to edit or delete a failure description
class AdminEditFailureDescriptionView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureDescriptionSerializer

    def get_object(self):

        return get_object_or_404(FailureDescription, exhibitId=self.kwargs["exhibitId"])
    
#curator view to edit or delete contributing factors
class AdminEditCotributingFactorsView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContributingFactorsSerilaizer

    def get_object(self):

        return get_object_or_404(ContributingFactors, exhibitId=self.kwargs["exhibitId"])
    

#curator view to create contributing factors
class AdminCreateContributingFactorView(CuratorProtectedView, generics.CreateAPIView):
    serializer_class = ContributingFactorsSerilaizer

    def perform_create(self, serializer):
        exhibit = get_object_or_404(Exhibit, exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

#curator view to create AI system description
class AdminCreateSystemDescView(CuratorProtectedView, generics.CreateAPIView):
    serializer_class = AiSystemDescriptionSerializer

    def perform_create(self, serializer):
        exhibit = get_object_or_404(Exhibit, exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

#curator view to create failure description
class AdminCreateFailureDescView(CuratorProtectedView, generics.CreateAPIView):
    serializer_class = FailureDescriptionSerializer

    def perform_create(self, serializer):
        exhibit = get_object_or_404(Exhibit, exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

#curator view to create lessons learned
class AdminCreateLessonLearnedView(CuratorProtectedView, generics.CreateAPIView):
    serializer_class = LessonsLearnedSerializer

    def perform_create(self, serializer):
        exhibit = get_object_or_404(Exhibit, exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

#view for registering a new account
def registerPage(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        #validate post request data
        if form.is_valid():
            user = form.save()
            #automattically assigned as a Visitor
            group = Group.objects.get(name='Visitor')
            user.groups.add(group)
            return redirect('login')

    context = {'form': form}
    return render(request, 'pages/register.html', context)

#view for logging in to your account
@rate_limiter
def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user()) 
            return redirect('exhibits')
    else:
        form = AuthenticationForm()
    
    return render(request, 'pages/login.html', {'form': form})

#view for logging out
def logoutUser(request):
    logout(request)
    return redirect('login')

#view for creating and viewing comments
class ExhibitCommentsView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    #get requests 
    def get_queryset(self):
        #get the request's exhibit object 
        exhibit = get_object_or_404(Exhibit, exhibitId=self.kwargs['exhibitId'])
        #filter comments to include only those who's exhibit matches and have been approved
        return Comments.objects.filter(exhibit=exhibit, isApproved=True)

    #post request to create a new comment
    def perform_create(self, serializer):
        exhibit = get_object_or_404(Exhibit, exhibitId=self.kwargs['exhibitId'])
        serializer.save(exhibit=exhibit, user=self.request.user)

#view for curators to view incoming comments
class CuratorIncomingCommentsView(CuratorProtectedView, generics.ListAPIView):
    serializer_class = CuratorCommentReviewSerializer

    #get request returns all unnapproverd comments
    def get_queryset(self):
        return Comments.objects.filter(isApproved=False)

#view to approve/delete a specific comment
class CuratorReviewCommentView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CuratorCommentReviewSerializer

    def get_object(self):
        return get_object_or_404(Comments, commentId=self.kwargs['commentId'])



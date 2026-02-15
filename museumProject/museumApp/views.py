from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import createUserForm
from django.contrib.auth import login, logout, authenticate

class UserExhibitsView(generics.ListAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer

class UserSingleExhibitView(generics.RetrieveAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    
class AdminExhibitsView(generics.ListCreateAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    
class AdminEditExhibitView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer

    
class AdminCreateArtefactView(generics.CreateAPIView):
    serializer_class = ArtefactSerializer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

class AdminEditArtefactView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtefactSerializer


    def get_queryset(self):
        return Artefact.objects.filter(exhibitId=self.kwargs["exhibitId"])


class AdminCreateContributingFactorView(generics.CreateAPIView):
    serializer_class = ContributingFactorsSerilaizer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

class AdminEditContributingFactorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContributingFactorsSerilaizer


    def get_queryset(self):
        return ContributingFactors.objects.filter(exhibitId=self.kwargs["exhibitId"])

class AdminCreateSystemDescView(generics.CreateAPIView):
    serializer_class = AiSystemDescriptionSerializer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibit=exhibit)

class AdminEditSystemDescView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AiSystemDescriptionSerializer

    def get_queryset(self):
        return AiSystemDescription.objects.filter(exhibitId=self.kwargs["exhibitId"])

class AdminCreateFailureDescView(generics.CreateAPIView):
    serializer_class = FailureDescriptionSerializer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibit=exhibit)

class AdminEditFailureDescView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureDescriptionSerializer


    def get_queryset(self):
        return FailureDescription.objects.filter(exhibitId=self.kwargs["exhibitId"])

class AdminCreateLessonLearnedView(generics.CreateAPIView):
    serializer_class = LessonsLearnedSerializer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

class AdminEditLessonLearnedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonsLearnedSerializer


    def get_queryset(self):
        return LessonsLearned.objects.filter(exhibitId=self.kwargs["exhibitId"])

from django.shortcuts import render, get_object_or_404
from .models import (
    Exhibit
)
from django.http import Http404


def registerPage(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'pages/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user()) 
            return redirect('exhibits')
    else:
        form = AuthenticationForm()
    
    return render(request, 'pages/login.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')
    #logout button to be added to html in order for this to work, and url path to be added to urls.py, otherwise pointless.






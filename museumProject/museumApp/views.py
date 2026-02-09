from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import createUserForm
from django.contrib.auth import login, logout, authenticate


class ExhibitsView(generics.ListCreateAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    
class SingleExhibitView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    
class ArtefactsView(generics.ListCreateAPIView):
    serializer_class = ArtefactSerializer

    def get_queryset(self):
        exhibit_id = self.kwargs["exhibit_id"]
        return Artefact.objects.filter(exhibitId=exhibit_id)
    
class SingleArtefactView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artefact.objects.all()
    serializer_class = ArtefactSerializer

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

    
    






from django.shortcuts import render, get_object_or_404
from .models import (
    Exhibit
)
from django.http import Http404

# def ExhibitsView(request):
#     exhibits = Exhibit.objects.all()
#     return render(request, "pages/exhibits.html", {"exhibits": exhibits})


# def SingleExhibitView(request, exhibit_id):
#     exhibit = get_object_or_404(Exhibit, exhibitId=exhibit_id)

#     artefacts = Artefact.objects.filter(exhibitId=exhibit)
#     ai_description = AiSystemDescription.objects.filter(exhibitId=exhibit).first()
#     contributing_factors = ContributingFactors.objects.filter(exhibitId=exhibit).first()
#     failures = FailureDescription.objects.filter(exhibitId=exhibit).first()
#     lessons = LessonsLearned.objects.filter(exhibitId=exhibit).first()

#     return render(request, "pages/single_exhibit.html", {
#         "exhibit": exhibit,
#         "artefacts": artefacts,
#         "ai_description": ai_description,
#         "contributing_factors": contributing_factors,
#         "failures": failures,
#         "lessons": lessons,
#     })

# def home(request):
#     return render(request, 'pages/home.html', {})

# def quiz(request, 
#          ):
#     return render(request, 'pages/quiz.html', {})

# def results(request,quizId ): 
#     question = get_object_or_404(QuizzQuestion, questionId=quizId)
#     return (response, "pags/options.html" )


# def results(request,quizId ): 
#     response = " "
#     return Http404


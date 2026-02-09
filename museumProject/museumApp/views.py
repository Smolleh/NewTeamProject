from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *


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
        return Artefact.objects.filter(exhibitId_id=self.kwargs["exhibitId"])


class AdminCreateContributingFactorView(generics.CreateAPIView):
    serializer_class = ContributingFactorsSerilaizer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

class AdminEditContributingFactorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContributingFactorsSerilaizer


    def get_queryset(self):
        return ContributingFactors.objects.filter(exhibitId_id=self.kwargs["exhibitId"])

class AdminCreateSystemDescView(generics.CreateAPIView):
    serializer_class = AiSystemDescriptionSerializer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibit=exhibit)

class AdminEditSystemDescView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AiSystemDescriptionSerializer

    def get_queryset(self):
        return AiSystemDescription.objects.filter(exhibit_id=self.kwargs["exhibitId"])

class AdminCreateFailureDescView(generics.CreateAPIView):
    serializer_class = FailureDescriptionSerializer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibit=exhibit)

class AdminEditFailureDescView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FailureDescriptionSerializer


    def get_queryset(self):
        return FailureDescription.objects.filter(exhibit_id=self.kwargs["exhibitId"])

class AdminCreateLessonLearnedView(generics.CreateAPIView):
    serializer_class = LessonsLearnedSerializer

    def perform_create(self, serializer):
        exhibit = Exhibit.objects.get(exhibitId=self.kwargs["exhibitId"])
        serializer.save(exhibitId=exhibit)

class AdminEditLessonLearnedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonsLearnedSerializer


    def get_queryset(self):
        return LessonsLearned.objects.filter(exhibitId_id=self.kwargs["exhibitId"])

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


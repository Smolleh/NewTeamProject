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
    serializer_class = SimpleViewExhibitSerializer

class UserSingleExhibitView(generics.RetrieveAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    
class AdminExhibitsView(generics.ListCreateAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = SimpleViewCreateExhibitSerializer
    
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



from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *


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
    

# Create your views here.

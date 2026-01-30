from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *


class exhibitsView(generics.ListCreateAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer

class singleExhibitView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer
    

# Create your views here.

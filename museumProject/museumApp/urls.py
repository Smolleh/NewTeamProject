from django.urls import path
from . import views

urlpatterns = [
     path('exhibits', views.ExhibitsView.as_view()), 
     path('exhibits/<int:pk>', views.SingleExhibitView.as_view()),
     path('artefacts/<int:exhibit_id>', views.ArtefactsView.as_view()),
     path('artefact/<int:pk>', views.SingleArtefactView.as_view()),
]


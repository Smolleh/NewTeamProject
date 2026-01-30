from django.urls import path
from . import views

urlpatterns = [
     path('exhibits', views.exhibitsView.as_view()), 
     path('exhibits/<int:pk>', views.singleExhibitView.as_view()),
]


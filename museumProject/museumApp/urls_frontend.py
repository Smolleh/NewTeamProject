from django.urls import path
from . import views_frontend

urlpatterns = [
    path("gallery/", views_frontend.exhibits, name="exhibits"),
    path("gallery/<int:exhibitId>/", views_frontend.singleExhibit, name="singleExhibit"),
    path("", views_frontend.home, name="home"),

]
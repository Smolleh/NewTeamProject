from django.urls import path
from . import views_frontend
from django.contrib.auth import views as auth

urlpatterns = [
    path("gallery/", views_frontend.exhibits, name="exhibits"),
    path("gallery/<int:exhibitId>/", views_frontend.singleExhibit, name="singleExhibit"),
    path("", views_frontend.home, name="home"),
    
    path("privacy-policy/", views_frontend.privacy_policy, name="privacy_policy"),
    path("about/", views_frontend.about, name="about"),
    
    path("login/", views_frontend.login, name="login"),
    path("logout/",  auth.LogoutView.as_view(template_name ='pages/home.html'), name ='logout'),
    path("register/", views_frontend.register, name="register")

]
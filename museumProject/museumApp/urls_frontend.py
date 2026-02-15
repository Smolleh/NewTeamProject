from django.urls import path
from . import views_frontend
from django.contrib.auth import views as auth

urlpatterns = [
    path("exhibit/", views_frontend.exhibits, name="exhibits"),
    path("exhibit/<int:exhibitId>/", views_frontend.single_exhibit, name="single_exhibit"),
    path("", views_frontend.home, name="home"),
    
    path("privacy_policy/", views_frontend.privacy_policy, name="privacy_policy"),
    path("about/", views_frontend.about, name="about"),
    
    path("login/", views_frontend.login, name="login"),
    path("logout/",  auth.LogoutView.as_view(template_name ='pages/home.html'), name ='logout'),
    path("register/", views_frontend.register, name="register"),
    
    path('curator_dashboard/', views_frontend.curator_dashboard, name='curator_dashboard'),
    path('system/<int:exhibitId>/', views_frontend.system, name='system'),

]
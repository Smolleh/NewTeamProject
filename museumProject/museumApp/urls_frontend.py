from django.urls import path
from . import views_frontend
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path("exhibit/", views_frontend.exhibits, name="exhibits"),
    path("exhibit/<int:exhibitId>/", views_frontend.single_exhibit, name="single_exhibit"),
    path("", views_frontend.home, name="home"),
    
    path("privacy_policy/", views_frontend.privacy_policy, name="privacy_policy"),
    path("about/", views_frontend.about, name="about"),
    
    path("login/", views.loginPage, name="login"),
    path("logout/",  auth.LogoutView.as_view(template_name ='pages/home.html'), name ='logout'),
    path("register/", views.registerPage, name="register"),
    
    path('curator_dashboard/', views_frontend.curator_dashboard, name='curator_dashboard'),
    
    path('system/<int:exhibitId>/', views_frontend.edit_system, name='edit_system'),
    path('lessons/<int:exhibitId>/', views_frontend.edit_lessons, name='edit_lessons'),
    path('failure/<int:exhibitId>/', views_frontend.edit_failure, name='edit_failure'),
    path('factors/<int:exhibitId>/', views_frontend.edit_factors, name='edit_factors'),
    path('exhibit_detail/<int:exhibitId>/', views_frontend.edit_exhibit_detail, name='edit_exhibit_detail'),
    path('artefect/<int:exhibitId>/<int:artefactID>/', views_frontend.edit_artefect, name='edit_artefect'),

    path('create_system/<int:exhibitId>/', views_frontend.create_system, name='create_system'),
    path('create_lessons/<int:exhibitId>/', views_frontend.create_lessons, name='create_lessons'),
    path('create_failure/<int:exhibitId>/', views_frontend.create_failure, name='create_failure'),
    path('create_factors/<int:exhibitId>/', views_frontend.create_factors, name='create_factors'),
    path('create_exhibit/', views_frontend.create_exhibit, name='create_exhibit'),
    path('create_artefect/<int:exhibitId>/', views_frontend.create_artefect, name='create_artefect'),

    path('quiz/', views_frontend.quiz, name='quiz'),
    path('single_quiz/<int:quizId>/', views_frontend.single_quiz, name='single_quiz'),
]
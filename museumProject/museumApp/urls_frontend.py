from django.urls import path
from . import views_frontend
from . import views
from django.contrib.auth import views as auth
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path("exhibit/", views_frontend.exhibits, name="exhibits"),
    path("exhibit/<int:exhibitId>/", views_frontend.single_exhibit, name="single_exhibit"),
    path('exhibit/<int:exhibitId>/bookmark/', views_frontend.bookmarkExhibit, name='bookmarkExhibit'),#new path for bookmark function 
    path('bookmarks/', views_frontend.bookmarkedExhibits, name='bookmarks'),#new path to view the bookmarked exhibits
    path('bookmarks/<int:exhibitId>/unbookmark/', views_frontend.unbookmarkExhibit, name='unbookmarkExhibit'),
    path('profile/edit/', views_frontend.edit_profile, name='edit_profile'),
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
    path('artefact/<int:exhibitId>/<int:artefactId>/', views_frontend.edit_artefact, name='edit_artefact'),

    path('create_system/<int:exhibitId>/', views_frontend.create_system, name='create_system'),
    path('create_lessons/<int:exhibitId>/', views_frontend.create_lessons, name='create_lessons'),
    path('create_failure/<int:exhibitId>/', views_frontend.create_failure, name='create_failure'),
    path('create_factors/<int:exhibitId>/', views_frontend.create_factors, name='create_factors'),
    path('create_exhibit/', views_frontend.create_exhibit, name='create_exhibit'),
    path('create_artefact/<int:exhibitId>/', views_frontend.create_artefact, name='create_artefact'),

    path('quiz/', views_frontend.quiz, name='quiz'),
    path('single_quiz/<int:quizId>/', views_frontend.single_quiz, name='single_quiz'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #needed for images 
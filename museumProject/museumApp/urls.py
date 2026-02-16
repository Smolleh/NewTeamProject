from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     #path('', views.home, name='home'),
     path('exhibits/', views.UserExhibitsView.as_view(), name = 'exhibits'),
     path('exhibits/<int:pk>', views.UserSingleExhibitView.as_view()),
     #view and create exhibits
     path('exhibits/viewCreate', views.AdminExhibitsView.as_view()),
     # view, edit and delete exhibit 
     path('exhibits/<int:pk>/edit', views.AdminEditExhibitView.as_view()),
     #crearte artefact
     path("exhibits/<int:exhibitId>/artefacts/new", views.AdminCreateArtefactView.as_view()),
     # view, edit and delete artefact
     path('exhibits/<int:exhibitId>/artefacts/edit/', views.AdminEditArtefactView.as_view()),
     #crearte System description
     path("exhibits/<int:exhibitId>/ai-system-description/new", views.AdminCreateSystemDescView.as_view()),
     # view, edit and delete system description
     path('exhibits/<int:exhibitId>/ai-system-description/edit/', views.AdminEditSystemDescView.as_view()),
     #crearte failure description
     path("exhibits/<int:exhibitId>/failure-description/new", views.AdminCreateFailureDescView.as_view()),
     # view, edit and delete failure description
     path('exhibits/<int:exhibitId>/failure-description/edit/', views.AdminEditFailureDescriptionView.as_view()),
     #crearte a lesson learned
     path("exhibits/<int:exhibitId>/lessons-learned/new", views.AdminCreateLessonLearnedView.as_view()),
     # view, edit and delete lessons learned
     path('exhibits/<int:exhibitId>/lessons-learned/edit/', views.AdminEditLessonsLearnedView.as_view()),
     #crearte contributing factor
     path("exhibits/<int:exhibitId>/contributing-factors/new", views.AdminCreateContributingFactorView.as_view()),
     # view, edit and delete contributing factors
     path('exhibits/<int:exhibitId>/contributing-factors/edit/', views.AdminEditCotributingFactorsView.as_view()),
     path('login/', views.loginPage, name='login'),
     path('register/', views.registerPage, name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


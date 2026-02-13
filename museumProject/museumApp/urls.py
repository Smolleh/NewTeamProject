from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     #view all exhibits
     path('exhibits/', views.UserExhibitsView.as_view()),
     #view a specifc exhibit
     path('exhibits/<int:pk>', views.UserSingleExhibitView.as_view()),
     #view and create exhibits
     path('exhibits/viewCreate', views.AdminExhibitsView.as_view()),
     # view, edit and delete exhibit 
     path('exhibits/<int:pk>/edit', views.AdminEditExhibitView.as_view()),
     #crearte artefact
     path("exhibits/<int:exhibitId>/artefacts/new", views.AdminCreateArtefactView.as_view()),
     # view, edit and delete artefact
     path('exhibits/<int:exhibitId>/artefacts/edit/<int:pk>', views.AdminEditArtefactView.as_view()),
     #crearte System description
     path("exhibits/<int:exhibitId>/aiSystemDescription/new", views.AdminCreateSystemDescView.as_view()),
     # view, edit and delete system description
     path('exhibits/<int:exhibitId>/aiSystemDescription/edit/<int:pk>', views.AdminEditSystemDescView.as_view()),
     #crearte failure description
     path("exhibits/<int:exhibitId>/failureDescription/new", views.AdminCreateFailureDescView.as_view()),
     # view, edit and delete failure description
     path('exhibits/<int:exhibitId>/failureDescription/edit/<int:pk>', views.AdminEditFailureDescView.as_view()),
     #crearte a lesson learned
     path("exhibits/<int:exhibitId>/lessonsLearned/new", views.AdminCreateLessonLearnedView.as_view()),
     # view, edit and delete lessons learned
     path('exhibits/<int:exhibitId>/lessonsLearned/edit/<int:pk>', views.AdminEditLessonLearnedView.as_view()),
     #crearte contributing factor
     path("exhibits/<int:exhibitId>/contributingFactors/new", views.AdminCreateContributingFactorView.as_view()),
     # view, edit and delete contributing factors
     path('exhibits/<int:exhibitId>/contributingFactors/edit/<int:pk>', views.AdminEditContributingFactorView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('exhibits/', views.UserExhibitsView.as_view()),
     path('exhibits/<int:pk>', views.UserSingleExhibitView.as_view()),
     path('exhibits/viewCreate', views.AdminExhibitsView.as_view()), 
     path('exhibits/<int:pk>/edit', views.AdminEditExhibitView.as_view()),
     path("exhibits/<int:exhibitId>/artefacts/new", views.AdminCreateArtefactView.as_view()),
     path('exhibits/<int:exhibitId>/artefacts/edit/<int:pk>', views.AdminEditArtefactView.as_view()),
     path("exhibits/<int:exhibitId>/aiSystemDescription/new", views.AdminCreateSystemDescView.as_view()),
     path('exhibits/<int:exhibitId>/aiSystemDescription/edit/<int:pk>', views.AdminEditSystemDescView.as_view()),
     path("exhibits/<int:exhibitId>/failureDescription/new", views.AdminCreateFailureDescView.as_view()),
     path('exhibits/<int:exhibitId>/failureDescription/edit/<int:pk>', views.AdminEditFailureDescView.as_view()),
     path("exhibits/<int:exhibitId>/lessonsLearned/new", views.AdminCreateLessonLearnedView.as_view()),
     path('exhibits/<int:exhibitId>/lessonsLearned/edit/<int:pk>', views.AdminEditLessonLearnedView.as_view()),
     path("exhibits/<int:exhibitId>/contributingFactors/new", views.AdminCreateContributingFactorView.as_view()),
     path('exhibits/<int:exhibitId>/contributingFactors/edit/<int:pk>', views.AdminEditContributingFactorView.as_view()),
     
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


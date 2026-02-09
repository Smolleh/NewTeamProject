from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     #path('', views.home, name='home'),
     path('exhibits/', views.ExhibitsView.as_view(), name='exhibits'), 
     path('exhibits/<int:pk>', views.SingleExhibitView.as_view(), name='single_exhibit'),
     path('artefacts/<int:pk>', views.ArtefactsView.as_view()),
     path('artefact/<int:pk>', views.SingleArtefactView.as_view()),
     path('register/', views.registerPage, name='register'),
     path('login/', views.loginPage, name='login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


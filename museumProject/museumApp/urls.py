from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.home, name='home'),
     path('exhibits/', views.ExhibitsView, name='exhibits'), 
     path('exhibits/<int:exhibit_id>', views.SingleExhibitView, name='single_exhibit'),
     #path('artefacts/<int:exhibit_id>', views.ArtefactsView),
     #path('artefact/<int:pk>', views.SingleArtefactView),
     #path('login/', views.login_view, name='login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


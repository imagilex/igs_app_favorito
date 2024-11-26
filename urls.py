from django.urls import include
from django.urls import path

urlpatterns = [
    path('favorito/', include('igs_app_favorito.favorito.urls')),
    ]

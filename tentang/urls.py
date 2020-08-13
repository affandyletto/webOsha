from django.urls import path
from django.views.generic import ListView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import re_path, include
from .views import profilView,legalitasView,strukturView,daftarAsesorView

app_name="tentang"
urlpatterns=[
	path('profil',profilView.as_view(),name="profil"),
	path('legalitas',legalitasView.as_view(),name="legalitas"),
	path('struktur',strukturView.as_view(),name="struktur"),
	path('daftarAsesor',daftarAsesorView.as_view(),name="daftarAsesor"),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
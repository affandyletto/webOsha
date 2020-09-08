from django.urls import path
from django.views.generic import ListView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import re_path, include
from .views import pengalamanView,permohonanView,kontak

app_name="pengalamanKontakForm"
urlpatterns=[
	path('pengalaman',pengalamanView,name="pengalaman"),
	path('kontak',kontak,name="kontak"),
	path('permohonan',permohonanView.as_view(),name="permohonan"),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
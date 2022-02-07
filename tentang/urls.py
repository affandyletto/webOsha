from django.urls import path
from django.views.generic import ListView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import re_path, include
from .views import profilView

app_name="tentang"
urlpatterns=[
	path('profil',profilView.as_view(),name="profil")
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
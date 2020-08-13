from django.urls import path
from django.views.generic import ListView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import re_path, include
from .views import ruangView,prosesView,alurView,regulasiView

app_name="sertifikasi"
urlpatterns=[
	path('ruang',ruangView.as_view(),name="ruang"),
	path('proses',prosesView.as_view(),name="proses"),
	path('alur',alurView.as_view(),name="alur"),
	path('regulasi',regulasiView.as_view(),name="regulasi"),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
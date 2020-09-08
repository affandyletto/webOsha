from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import sejarah,jab,sub,daftarAsesor,bidang,strukturOrganisasi,legalitas,bidangUtama
@admin.register(sejarah)
@admin.register(jab)
@admin.register(sub)
@admin.register(daftarAsesor)
@admin.register(bidang)
@admin.register(strukturOrganisasi)
@admin.register(legalitas)
@admin.register(bidangUtama)
class user(ImportExportModelAdmin):
	pass
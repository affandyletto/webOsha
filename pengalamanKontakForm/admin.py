from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import profile, partner,pengalaman,dokumentasi,visi,misi,judulGallery,jenisGallery
@admin.register(profile)
@admin.register(partner)
@admin.register(pengalaman)
@admin.register(dokumentasi)
@admin.register(visi)
@admin.register(misi)
@admin.register(judulGallery)
@admin.register(jenisGallery)
class user(ImportExportModelAdmin):
	pass
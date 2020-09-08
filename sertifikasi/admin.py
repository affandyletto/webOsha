from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import subBidang,bidang 
@admin.register(subBidang)
@admin.register(bidang)
class user(ImportExportModelAdmin):
	pass
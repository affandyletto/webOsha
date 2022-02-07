from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView

class profilView(TemplateView):
	template_name="tentang/profil.html"

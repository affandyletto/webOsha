from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,RedirectView,DetailView,UpdateView,CreateView,TemplateView

class profilView(TemplateView):
	template_name="tentang/profil.html"

class legalitasView(TemplateView):
	template_name="tentang/legalitas.html"

class daftarAsesorView(TemplateView):
	template_name="tentang/daftarasesor.html"

class strukturView(TemplateView):
	template_name="tentang/strukturorganisasi.html"
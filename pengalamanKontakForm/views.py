from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,RedirectView,DetailView,UpdateView,CreateView,TemplateView

class pengalamanView(TemplateView):
	template_name="pengalamanKontakForm/dokumentasi.html"

class kontakView(TemplateView):
	template_name="pengalamanKontakForm/kontak.html"

class permohonanView(TemplateView):
	template_name="pengalamanKontakForm/permohonan.html"
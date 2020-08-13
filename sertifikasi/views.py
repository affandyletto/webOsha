from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,RedirectView,DetailView,UpdateView,CreateView,TemplateView

class ruangView(TemplateView):
	template_name="sertifikasi/ruang.html"

class prosesView(TemplateView):
	template_name="sertifikasi/proses.html"

class alurView(TemplateView):
	template_name="sertifikasi/alur.html"

class regulasiView(TemplateView):
	template_name="sertifikasi/regulasi.html"
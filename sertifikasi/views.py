from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView

class ruangView(TemplateView):
	template_name="sertifikasi/ruang.html"

from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,RedirectView,DetailView,UpdateView,CreateView,TemplateView
from pengalamanKontakForm.models import profile,partner,visi,misi
from tentang.models import legalitas

class berandaView(TemplateView):
	template_name="index.html"

def beranda(request):
	context={
		'profile':profile.objects.all(),
		'partner':partner.objects.all(),
		'visi':visi.objects.all(),
		'misi':misi.objects.all(),
		'sesuatu':legalitas.objects.all()
	}
	return render(request,'index.html',context)
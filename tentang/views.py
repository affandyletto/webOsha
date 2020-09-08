from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,RedirectView,DetailView,UpdateView,CreateView,TemplateView
from .models import legalitas,strukturOrganisasi,bidang,daftarAsesor,sub,jab,bidangUtama

class profilView(TemplateView):
	template_name="tentang/profil.html"

def legalitasView(request):
	context={
		'sesuatu':legalitas.objects.all()
	}
	return render(request,'tentang/legalitas.html',context)

def daftarAsesorView(request):
	context={
		'sesuatu':daftarAsesor.objects.all().filter(bidang__in=bidangUtama.objects.filter(bidang="BIDANG DISTRIBUSI TENAGA LISTRIK")),
		'sesuatuAja':daftarAsesor.objects.all().filter(bidang__in=bidangUtama.objects.filter(bidang="BIDANG PEMBANGKIT TENAGA LISTRIK"))
	}
	return render(request,'tentang/daftarasesor.html',context)

def strukturView(request):
	sesuatu=bidang.objects.all()		
	context={
		'sesuatu':strukturOrganisasi.objects.all(),
		'komisaris':strukturOrganisasi.objects.filter(status__in=bidang.objects.filter(namaBidang="Dewan Komisaris")),
		'direksi':strukturOrganisasi.objects.filter(status__in=bidang.objects.filter(namaBidang="Jajaran Direksi")),
		'distribusi':strukturOrganisasi.objects.filter(status__in=bidang.objects.filter(namaBidang="Bidang Distribusi")),
		'pembangkitan':strukturOrganisasi.objects.filter(status__in=bidang.objects.filter(namaBidang="Bidang Pembangkitan")),
		'manager':strukturOrganisasi.objects.filter(status__in=bidang.objects.filter(namaBidang="Manajer Sertifikasi")),
		'seksi':strukturOrganisasi.objects.filter(status__in=bidang.objects.filter(namaBidang="Seksi")),
	}
	return render(request,'tentang/strukturorganisasi.html',context)
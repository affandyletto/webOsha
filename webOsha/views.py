from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView
from pengalamanKontakForm.models import partner


class berandaView(TemplateView):
	template_name="index.html"

def beranda(request):
	context={
		'partner':partner.objects.all()
	}
	return render(request,'index.html',context)
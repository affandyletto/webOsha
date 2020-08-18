from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,RedirectView,DetailView,UpdateView,CreateView,TemplateView
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.contrib import messages

class pengalamanView(TemplateView):
	template_name="pengalamanKontakForm/dokumentasi.html"

class permohonanView(TemplateView):
	template_name="pengalamanKontakForm/permohonan.html"
def kontak(request):
	if request.method=="POST":
		nama=request.POST['nama']		
		email=request.POST['email']
		telp=request.POST['telp']
		kota=request.POST['kota']
		isi=request.POST['isi']

		print(nama)
		message=EmailMessage("Pesan dari web Osha","Nama : "+nama+"\n Email: "+email+"\nTelp: "+telp+"\nKota: "+kota+"\nPesan : "+isi,
		"SDM",["osha.eleska.ind@gmail.com"])
		message.send()
		messages.success(request, 'Pesan telah dikirim ke Email kami')		
	context={}

	return render(request,'pengalamanKontakForm/kontak.html',context)
from django.shortcuts import render,redirect
from django.views import View
from django.core import mail
from django.core.mail import send_mail,EmailMessage
from django.views.generic import TemplateView
from django.contrib import messages

class ruangView(TemplateView):
	template_name="sertifikasi/ruang.html"

def uploadPermohonan(request):

	if request.method =='POST':
		foto = request.FILES["foto1"]
		ktp = request.FILES["ktp"]
		ijazah = request.FILES["ijazah"]
		dokumen = request.FILES["dokumen"]
		email = request.POST["email"]
		filename=[foto,ktp,ijazah,dokumen]
		connection = mail.get_connection()
		connection.open()
		message=EmailMessage("Permohonan Sertifikasi Kompetensi Baru",
			"Berikut dokumen Permohonan sertifikasi kompetensi baru dari dari email :"+email,
			"SDM",["letto.affandy@gmail.com","osha.eleska.ind@gmail.com"],connection=connection)

		message.attach(foto.name,foto.read(),foto.content_type)
		message.attach(ktp.name,ktp.read(),ktp.content_type)
		message.attach(ijazah.name,ijazah.read(),ijazah.content_type)
		message.attach(dokumen.name,dokumen.read(),dokumen.content_type)
		message.send()
		connection.close()
		messages.success(request, 'anda telah mengirim email kepada kami')
		return redirect('sertifikasi:ruang')

	return redirect('sertifikasi:ruang')

def uploadPerpanjangan(request):	
	if request.method =='POST':
		foto = request.FILES["foto1"]
		ktp = request.FILES["ktp"]
		sertifikat = request.FILES["sertifikat"]
		dokumen = request.FILES["dokumen"]
		email = request.POST["email"]
		connection = mail.get_connection()
		connection.open()
		message=EmailMessage("Permohonan Sertifikasi Kompetensi Baru",
			"Berikut dokumen Permohonan sertifikasi kompetensi baru dari dari email :"+email,
			"SDM",["letto.affandy@gmail.com","osha.eleska.ind@gmail.com"],connection=connection)
		message.attach(foto.name,foto.read(),foto.content_type)
		message.attach(ktp.name,ktp.read(),ktp.content_type)
		message.attach(sertifikat.name,sertifikat.read(),sertifikat.content_type)
		message.attach(dokumen.name,dokumen.read(),dokumen.content_type)

		message.send()
		connection.close()
		messages.success(request, 'anda telah mengirim email kepada kami')
		return redirect('sertifikasi:ruang')

	return redirect('sertifikasi:ruang')
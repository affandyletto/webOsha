from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize
# Create your models here.
class legalitas(models.Model):
	nama=models.CharField(max_length=255,default="")
	image=models.FileField(default="")
	smart=ImageSpecField(
		source="image",format="JPEG",
		options={'quality':30}
		)		

	def __str__(self):
		return "{}".format(self.nama)

class sejarah(models.Model):
	text=models.TextField()

	def __str__(self):
		return "{}".format(self.text)

class jab(models.Model):
	namaJabatan=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.namaJabatan)

class sub(models.Model):
	namaSub=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.namaSub)

class bidangUtama(models.Model):
	bidang=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.bidang)

class daftarAsesor(models.Model):
	namaAsesor=models.CharField(max_length=255,default="")
	jabatan=models.ManyToManyField(jab, default="",blank=True)
	subBidang=models.ManyToManyField(sub, default="",blank=True)
	bidang=models.ManyToManyField(bidangUtama,default="",blank=True)

	def __str__(self):
		return "{}".format(self.namaAsesor)

class bidang(models.Model):
	namaBidang=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.namaBidang)

class strukturOrganisasi(models.Model):
	nama=models.CharField(max_length=255,default="")
	keterangan=models.CharField(max_length=255,default="")
	status=models.ManyToManyField(bidang, default="",blank=True)
	foto=models.FileField(default="",blank=True,null=True)
	
	smart=ImageSpecField(
		source="foto",format="JPEG",
		options={'quality':50}
		)
	def __str__(self):
		return "{}".format(self.nama)










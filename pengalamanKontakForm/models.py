from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize

class profile(models.Model):
	text=models.TextField()

	def __str__(self):
		return "{}".format(self.text)

class partner(models.Model):
	nama=models.CharField(max_length=255,default="")
	image=models.FileField(default="")
	smart=ImageSpecField(
		source="image",format="JPEG",
		options={'quality':30}
		)
	
	def __str__(self):
		return "{}".format(self.nama)

class visi(models.Model):
	visi=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.visi)

class misi(models.Model):
	misi=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.misi)

class pengalaman(models.Model):
	jenis=models.CharField(max_length=255,default="")
	tgl=models.CharField(max_length=255,default="")
	keterangan=models.CharField(max_length=255,default="")

	def __str__(self):
		return "{}".format(self.jenis)

class judulGallery(models.Model):
	judul=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.judul)

class jenisGallery(models.Model):
	jenis=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.jenis)

class dokumentasi(models.Model):
	judul=models.ManyToManyField(judulGallery,default="",blank=True)
	jenis=models.ManyToManyField(jenisGallery,default="",blank=True)
	image=models.FileField(default="")
	smart=ImageSpecField(
		source="image",format="JPEG",
		options={'quality':30}
		)
	def __str__(self):
		return "{}".format(self.image)
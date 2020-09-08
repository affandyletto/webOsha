from django.db import models

# Create your models here.
class subBidang(models.Model):
	namaSub=models.CharField(max_length=255,default="")
	def __str__(self):
		return "{}".format(self.namaSub)

class bidang(models.Model):
	bidang=models.CharField(max_length=255,default="")
	subBidang=models.ManyToManyField(subBidang, default="",blank=True)

	def __str__(self):
		return "{}".format(self.bidang)
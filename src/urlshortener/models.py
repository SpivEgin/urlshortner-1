from __future__ import unicode_literals

from django.db import models

# Create your models here.

class KirrURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode  = models.CharField(max_length=20)
	#shortcode  = models.CharField(max_length=20, default="shortcode")

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	def 

		
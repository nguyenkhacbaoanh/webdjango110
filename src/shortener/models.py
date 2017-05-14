from django.db import models
from .utils import code_generator, create_shortcode
# Create your models here.

#Mode manager and refresh shortcode
class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(KirrURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs


class KirrURL(models.Model):
	url 		= models.CharField(max_length=220)
	shortcode 	= models.CharField(max_length=15, unique=True, blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	active		= models.BooleanField(default=True)

	objects 	= KirrURLManager()
	#some_random = KirrURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode == None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(KirrURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
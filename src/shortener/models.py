from django.db import models
import string
import random

# Create your models here.
def code_generator(size=6, chars=string.acsii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

class KirrURL(models.Model):
	url 		= models.CharField(max_length=220)
	shortcode 	= models.CharField(max_length=15, unique=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	def save(self, *args, **kwa):
		self.shortcode = code_generator()
		super(KirrURL, self).save(*args, **kwa)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
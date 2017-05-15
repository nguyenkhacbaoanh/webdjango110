from django.db import models
from .utils import code_generator, create_shortcode
# Create your models here.

<<<<<<< HEAD
class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(KirrURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=False)
		return qs
	def refresh_shortcodes(self):
		qs = KirrURL.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_codes += 1
		return "New codes made {}".format(new_codes)

=======
#Mode manager and refresh shortcode
class KirrURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(KirrURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs
>>>>>>> 0d775021519b785de0045875c6eec76cd9c12116


class KirrURL(models.Model):
	url 		= models.CharField(max_length=220)
	shortcode 	= models.CharField(max_length=15, unique=True, blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	active		= models.BooleanField(default=True)

<<<<<<< HEAD
	#mode_random = KirrURLManager()
	objects = KirrURLManager()


=======
	objects 	= KirrURLManager()
	#some_random = KirrURLManager()
>>>>>>> 0d775021519b785de0045875c6eec76cd9c12116

	def save(self, *args, **kwargs):
		if self.shortcode == None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(KirrURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
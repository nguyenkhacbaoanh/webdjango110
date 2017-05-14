import string
import random

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
	new_code = code_generator(size=6)
	kirrURL = instance.__class__
	qs_exist = kirrURL.objects.filter(new_code).exists()
	if qs_exist:
		return create_shortcode()
	return new_code
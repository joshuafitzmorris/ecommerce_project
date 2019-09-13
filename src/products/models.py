from django.db import models
import random
import os

def get_filename_ext(filename):
	base_name = os.path.basename(filename)
	name, ext = os.path.splitext(filename)
	return name, ext

# Create your models here.

def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename = random.randint(1,4219048129)
	name, ext = get_filename_ext(filename)
	final_filename ='{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(
		new_filename = new_filename,
		final_filename=final_filename
		)

class ProductManager(models.Manager):
	def get_by_id(self,id):
		return self.get_queryset(id=id)


class Product(models.Model):
	title		= models.CharField(max_length=120)
	description = models.TextField()
	price		= models.DecimalField(decimal_places=2, max_digits=20, default=79.99)
	image		= models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	def __str__(self):
		return self.title
	
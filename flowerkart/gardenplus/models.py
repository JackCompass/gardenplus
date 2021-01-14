from django.db import models

# Create your models here.

class Products(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(default = 'This is one of the main product of our company.')
	price = models.FloatField()
	img = models.ImageField(upload_to = 'images/', default='Not Available')

	def __str__(self):
		return f"{self.name}"
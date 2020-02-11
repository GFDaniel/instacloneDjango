from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	name = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
	imageProfile = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
	image = models.ImageField(blank=True, null=True)
	caption = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.caption


andresbarbosa@useitweb.com
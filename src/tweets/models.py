from django.conf import settings
from django.db import models

# Create your models here.


class Tweet(models.Model):
	user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content     = models.CharField(max_length=140)
	updated     = models.DateTimeField(auto_now=True)
	timestamp   = models.DateTimeField(auto_now_add=True)
	def _str_(self):
		return self.content
	

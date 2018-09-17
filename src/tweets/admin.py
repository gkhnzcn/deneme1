from django.contrib import admin


# Register your models here.
from .forms import TweetModelForm
from .models import Tweet 




class TweetModelAdmin(admin.ModelAdmin):
	class Meta:
		#model = Tweet
		form = TweetModelForm


	admin.site.register(Tweet, TweetModelAdmin)	
from django.db import models

# Create your models here.
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=200) 

class Watchlist(models.Model):
     title = models.CharField(max_length=50)
     type = models.CharField(max_length=50)
     description = models.CharField(max_length=500)  
     active = models.BooleanField(default=True)
     created = models.DateTimeField(auto_now_add=True)

# class Movies(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)
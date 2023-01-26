from django.db import models

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=80)
    contentRating = models.CharField(max_length=80)
    genre = models.CharField(max_length=80)
    installs = models.CharField(max_length=80)
    url = models.CharField(max_length=80)

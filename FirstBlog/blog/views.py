from django.shortcuts import render
from django.db import models
# Create your views here.

class posts(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

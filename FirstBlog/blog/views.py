from django.shortcuts import render
from django.db import models
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class PythonPageView(TemplateView):
    template_name = "python.html"

class CPageView(TemplateView):
    template_name = "c.html"

class CPlusPlusPageView(TemplateView):
    template_name = "c++.html"

class JavaPageView(TemplateView):
    template_name = "java.html"
'''
class posts(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
'''

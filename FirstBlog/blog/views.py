from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.views.generic import TemplateView, FormView
from .models import File
from .forms import FileForm
from django.core.files.storage import FileSystemStorage

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

class FilePageView(FormView):
    template_name = "file.html"
    success_url = '/success/'
    form_class = FileForm

    def form_valid(self, form):
        return HttpResponse("Sweeeet")

class CompiledFilePageView(TemplateView):
    template_name = "compiled_files.html"

def file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileForm()
    return render(request, '/file.html', {
        'form': form
    })

'''
class posts(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
'''

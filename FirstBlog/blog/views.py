from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from .models import File
from .forms import FileForm
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

def python(request):
    file = request.FILES.get('file_upload')
    files = File.objects.all()
    file_json = json.dumps(list(files), cls=DjangoJSONEncoder)

    return render(
        request,
        'python.html',
        {
            'files': files,
            'file': file,
            'files_json': files_json
        }
    )

def c(request):
    file = request.FILES.get('file_upload')
    files = File.objects.all()
    return render(
        request,
        'c.html',
        {
            'files': files
        }
    )

def cplusplus(request):
    file = request.FILES.get('file_upload')
    files = File.objects.all()
    return render(
        request,
        'c++.html',
        {
            'files': files
        }
    )

def java(request):
    file = request.FILES.get('file_upload')
    files = File.objects.all()
    return render(
        request,
        'java.html',
        {
            'files': files
        }
    )

def compiled_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file_upload']
            form.save() #Saving form model

            # Redirect to the file list after POST
            return HttpResponseRedirect(reverse('compiled_files_page'))
    else:
        form = FileForm()

    #Upload all files for file page
    files = File.objects.all()
    return render(
        request,
        'compiled_files.html',
        {
            'form': form,
            'files': files
        }
    )

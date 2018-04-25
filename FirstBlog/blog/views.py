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
class CompiledFilesPageView(TemplateView):
    template_name = "compiled_files.html"
'''
def compiled_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            usr_file = File(file_upload = request.FILES['file_upload'])
            usr_file.save()

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

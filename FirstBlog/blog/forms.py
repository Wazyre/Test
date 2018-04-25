from django import forms
from django.forms import ModelForm
from django.db import models
from blog import models
from django.utils import timezone

LANGUAGES = (
    ('C', 'C'),
    ('CPP', 'C++'),
    ('JAVA', 'Java'),
    ('PY', 'Python'),
)

class FileForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = models.File
        fields = ['author', 'name', 'description', 'language', 'file_upload', 'upload_date']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Hello World!'}),
            'description': forms.TextInput(attrs={'placeholder': 'This program does...'}),
            'upload_date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
            'upload_date': forms.DateInput(format = "%d-%m-%Y")
        }

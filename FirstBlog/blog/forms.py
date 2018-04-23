from django import forms
from django.forms import ModelForm
from .models import File
from django.utils import timezone

LANGUAGES = (
    ('C', 'C'),
    ('CPP', 'C++'),
    ('JAVA', 'Java'),
    ('PY', 'Python'),
)

class FileForm(ModelForm):
    error_css_class = 'error'

    #author = forms.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 500)
    language = forms.ChoiceField(choices = LANGUAGES, required = True)
    file_upload = forms.FileField(
        #required = True,
        label = 'Upload a file',
        help_text = '(max. 100 MB)'
        )

    upload_date = forms.DateTimeField()

    class Meta:
        model = File
        fields = ('file_upload',)

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'What\'s your name?'}),
            'description': forms.TextInput(attrs={'placeholder': 'This program does...'}),
            'upload_date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
        }

from django import forms
from .models import File

LANGUAGES = (
    ('C', 'C'),
    ('CPP', 'C++'),
    ('JAVA', 'Java'),
    ('PY', 'Python'),
)

class FileForm(forms.ModelForm):
    error_css_class = 'error'

    language = forms.ChoiceField(choices = LANGUAGES, required = True)
    file_upload = forms.FileField(required = True)

    class Meta:
        model = File
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'What\'s your name?'}),
            'description': forms.TextInput(attrs={'placeholder': 'This program does...'}),
            'upload_date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
        }

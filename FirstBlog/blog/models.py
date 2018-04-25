from django.db import models
from django.utils import timezone
from django import forms
from django.forms import ModelForm

# Create your models here.
LANGUAGES = (
    ('C', 'C'),
    ('CPP', 'C++'),
    ('JAVA', 'Java'),
    ('PY', 'Python'),
)
'''upload_to = language.choices + '/'''
class File(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    '''created_date = models.DateTimeField(
            default=timezone.now)'''
    language = models.CharField(max_length = 6, choices = LANGUAGES, null = True)
    file_upload = models.FileField(null = True, upload_to = 'files/%Y/%m/%d/')
    upload_date = models.DateTimeField(null = True, auto_now_add = True)

    def upload(self):
        self.upload_date = timezone.now()
        self.save()

    def __str__(self):
        """
        String for representing the File object (in Admin site etc.)
        """
        return self.name

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




'''
class MyModelName(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta:
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

# Create a new record using the model's constructor.
a_record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
a_record.save()

# Access model field values using Python attributes.
print(a_record.id) #should return 1 for the first record.
print(a_record.my_field_name) # should print 'Instance #1'

# Change record by modifying the fields, then calling save().
a_record.my_field_name="New Instance Name"
a_record.save()
'''

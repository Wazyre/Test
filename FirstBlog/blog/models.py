import os
import uuid

from django.db import models
from django.utils import timezone
from django import forms
from django.forms import ModelForm
from datetime import datetime, date
from FirstBlog import settings
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_delete
#from .utils import file_cleanup
# Create your models here.
LANGUAGES = (
    ('C', 'C'),
    ('CPP', 'C++'),
    ('JAVA', 'Java'),
    ('PY', 'Python'),
)


class File(models.Model):

    author = models.ForeignKey('auth.User', on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)
    '''created_date = models.DateTimeField(
            default=timezone.now)'''
    language = models.CharField(max_length = 6, choices = LANGUAGES, null = True)
    file_upload = models.FileField(null = True, upload_to = 'files/')
    upload_date = models.DateField(default = date.today, blank = True)

    def __str__(self):
        """
        String for representing the File object (in Admin site etc.)
        """
        return self.name

    def css_class(self):
        name, extension = os.path.splitext(self.file_upload.name)
        if extension == 'py':
            return "py"
        elif extension == 'c':
            return "c"
        elif extension == 'cpp':
            return "cpp"
        elif extension == 'java':
            return "java"
        else:
            return "other"
        return

    def delete(self,*args,**kwargs):
        if os.path.isfile(self.file_upload.path):
            os.remove(self.file_upload.path)

        super(File, self).delete(*args,**kwargs)

def file_cleanup(sender, **kwargs):
    """
    File cleanup callback used to emulate the old delete
    behavior using signals. Initially django deleted linked
    files when an object containing a File/ImageField was deleted.

    Usage:
    >>> from django.db.models.signals import post_delete
    >>> post_delete.connect(file_cleanup, sender=MyModel, dispatch_uid="mymodel.file_cleanup")
    """
    for fieldname in sender._meta.get_all_field_names():
            try:
                field = sender._meta.get_field(fieldname)
            except:
                field = None
                if field and isinstance(field, File):
                    inst = kwargs['instance']
                    f = getattr(inst, fieldname)
                    m = inst.__class__._default_manager
                    if hasattr(f, 'path') and os.path.exists(f.path)\
                    and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)})\
                    .exclude(pk=inst._get_pk_val()):
                        try:
                            FileSystemStorage.delete(f.path)
                        except:
                            pass

post_delete.connect(file_cleanup, sender=File, dispatch_uid="File.file_cleanup")
    # These two auto-delete files from filesystem when they are unneeded:
'''
@receiver(models.signals.post_delete, sender=File)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `File` object is deleted.
    """
    if instance.file_upload:
        if os.path.isfile(instance.file_upload.path):
            os.remove(instance.file_upload.path)

@receiver(models.signals.pre_save, sender=File)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `File` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = File.objects.get(pk=instance.pk).file_upload
    except File.DoesNotExist:
        return False

    new_file = instance.file_upload
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    def clean(self):
        cleaned_data = super(File, self).clean()
        file = cleaned_data.get('file_upload')

        if file:
            filename = file.name
            print(filename)
            if filename.endswith('.py', '.c', '.cpp', '.java'):
                print('File is valid')
            else:
                print('File is invalid')
                raise forms.ValidationError("File is invalid. Please upload only permitted language files")

        return file






input_formats = settings.DATE_INPUT_FORMATS,


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

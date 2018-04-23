from django.db import models
from django.utils import timezone

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

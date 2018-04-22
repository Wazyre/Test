# Generated by Django 2.0.4 on 2018-04-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180421_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_upload',
            field=models.FileField(null=True, upload_to='compiled_files/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='file',
            name='language',
            field=models.CharField(choices=[('C', 'C'), ('CPP', 'C++'), ('JAVA', 'Java'), ('PY', 'Python')], max_length=6, null=True),
        ),
    ]
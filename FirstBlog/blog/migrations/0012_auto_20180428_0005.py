# Generated by Django 2.0.4 on 2018-04-28 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180425_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_upload',
            field=models.FileField(null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='file',
            name='upload_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]

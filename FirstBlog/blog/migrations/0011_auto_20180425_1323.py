# Generated by Django 2.0.4 on 2018-04-25 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180425_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='upload_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]

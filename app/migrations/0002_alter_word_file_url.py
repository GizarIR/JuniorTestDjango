# Generated by Django 4.1.3 on 2022-11-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='file_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

from django.db import models

class Word(models.Model):
    text = models.CharField(
        unique=True,
        max_length=64,
    )
    num = models.IntegerField()
    file_url = models.CharField(
        max_length=255,
        blank=True,
    )

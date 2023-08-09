from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.model):

    class Status(models.TextChoices):
        # DRAFT: use as a variabl in the application, Df: in the database, Draft: human readable format
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    publish = models.DateTimeField(default=timezone.now())

    # auto_now save automatically when we save the object , save == updated 
    updated = models.DateTimeField(auto_now = True) 
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    class Meta:
        ordering = ['-publish']
        index = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

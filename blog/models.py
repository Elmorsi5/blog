from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    published = models.DateTimeField(default=timezone.now())
    
    # auto_now save automatically when we save the object , save == updated 
    updated = models.DateTimeField(auto_now = True) 

    def __str__(self):
        return self.title

from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status = Post.Status.PUBLISHED)



class Post(models.Model):

    class Status(models.TextChoices):
        # DRAFT(names): use as a variabl in the application, Df(vallues): in the database, Draft(labels):human readable format
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    publish = models.DateTimeField(default=timezone.now)

    # auto_now save automatically when we save the object , save == updated 
    updated = models.DateTimeField(auto_now = True) 
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    # on_delete: defint the behavior when the referenced object is deleted ( the user )
    # Related_name : We use it to access the posts of a specific user using this format:(user.blog_posts) 

    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')

    #Model fields:
    objects = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.id])

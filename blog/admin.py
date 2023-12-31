from django.contrib import admin
from .models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'title','slug','author','publish','status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    # Note: The value of the 'prepopulated_fields' must be a list or tuple 
    prepopulated_fields = {'slug': ('title',),} 
    # raw_id_fields: the author field is now displayed with a lookup widget, which can be much better than a drop-down select input when you have thousands of users 
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
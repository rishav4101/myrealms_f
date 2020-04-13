from django.db import models
from django.utils import timezone
from django.conf import settings 
from django.contrib.auth.models import User

class CategoryField(models.CharField):
    def __init__(self, *args, **kwargs):
        super (CategoryField, self).__init__(*args, **kwargs)
    def get_prep_value(self, value):
        return str(value).upper()

class Category(models.Model):
    name = CategoryField(max_length=20)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=10000)
    image = models.UrlField(max_length=1000)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    created_by = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)
    category1 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category1')
    category2 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category2')

    def __str__(self):
        return str('{} by {} on {}'.format(self.title, self.created_by, self.timestamp))

    def increase(self):
        self.views += 1
        self.save()
    
    class Meta:
        ordering = ['-timestamp']
    

class PostHits(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField(max_length=200)
    session = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return "Commented on post by {}".format(self.post.title, self.name)

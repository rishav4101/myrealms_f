from django.db import models
from django.utils import timezone
from django.conf import settings 
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=10000)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    hits = models.IntegerField(default=0)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return str('post by {} on {}'.format(self.created_by, self.created_at))

    def increase(self):
        self.hits += 1
        self.save()

class PostHits(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField(max_length=200)
    session = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)

class Contact(models.Model):
    email = models.EmailField(null=False)
    name = models.CharField(max_length=200,null=False)
    query = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    replied = models.BooleanField(default=False)

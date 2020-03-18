from django.db import models
from django.utils import timezone
from django.conf import settings 
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=400)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return str('post by {} on {}'.format(self.name, self.timestamp))

    def increase(self):
        self.hits += 1
        self.save()

class PostHits(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField(max_length=200)
    session = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
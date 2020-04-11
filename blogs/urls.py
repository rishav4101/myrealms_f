from .views import *
from django.urls import path, include

urlpatterns = [

    path('', index, name='index'),

    path('about', about, name='about'),

    path('team', team, name='team'),

    path('allPosts', allPosts, name='all_posts'),
    
    path('allPosts/post/<int:post_id>/', view_post, name='view_post' ),

]
from .views import *
from django.urls import path, include

urlpatterns = [

    path('', index, name='index'),

    path('about', about, name='about'),

    path('contact_us/', contact, name='contact'),

    path('allPosts', allPosts, name='all_posts'),
    
    path('allPosts/post/<int:post_id>/', view_post, name='view_post' ),

    path('allPosts/post/create', add_post, name='add_post' ),

    path('allPosts/post/update/<int:post_id>/', update_post, name='update_post' ),

    path('allPosts/comement/update/<int:comment_id>/', update_comment, name='update_comment' ),

    path('allPosts/comement/delete/<int:comment_id>/', delete_comment, name='delete_comment' ),

]
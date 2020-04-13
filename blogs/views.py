from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.shortcuts import redirect,render,get_object_or_404,reverse
from django.utils import timezone
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    posts = Post.objects.order_by('-timestamp')[:3]
    return render(request, 'blogs/home.html', {'posts':posts})

def about(request):
    return render(request, 'blogs/about_us.html')

def team(request):
    return render(request, 'blogs/team.html')

def allPosts(request):
    allPosts = Post.objects.order_by('-timestamp')
    paginator = Paginator(allPosts, 5)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blogs/posts_list.html', {'page': page, 'posts': posts})

def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    try:
        next_post = post.get_next_by_timestamp()
    except:
        next_post = None
    try:
        prev_post = post.get_previous_by_timestamp()
    except:
        prev_post = None

    # if not PostHits.objects.filter(post=post, session=request.session.session_key) :
    #     view = PostHits(post=post, ip=request.META['REMOTE_ADDR'], timestamp=timezone.now(), session=request.session.session_key)
    #     view.save()
    #     post.increase()
    comments = post.comments.filter(active=True)
    comment_form = CommentForm()
    new_comment = None
    if request.method == 'POST':
        comment_form  = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.created_on = timezone.now()
            new_comment.active = True
            new_comment = comment_form.save()
    return render(request, 'blogs/post.html', {'post':post, 'next': next_post, 'prev':prev_post, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form})





from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.shortcuts import redirect,render,get_object_or_404,reverse
from django.urls import reverse
from django.utils import timezone
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'blogs/index.html')


def allPosts(request):
    allPosts = Post.objects.order_by('-timestamp')
    page = request.GET.get('page', 1)
    paginator = Paginator(allPosts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'core/posts_list.html', {'posts': posts})
    

def viewPost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if not PostHits.objects.filter(post=post, session=request.session.session_key) :
        view = PostHits(post=post, ip=request.META['REMOTE_ADDR'], created=timezone.now(), session=request.session.session_key)
        view.save()
        post.increase()
    comments = post.comments.filter(active=True)
    comment_form = CommentForm()
    new_comment = None
    if request.method == 'POST':
        comment_form  = CommentForm(data=request.POST)
        if comment_form.is_valid():
            if not (request.user.is_authenticated):
                return redirect('login')
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.username = request.user
            new_comment.created_on = timezone.now()
            new_comment.active = True
            new_comment = comment_form.save()
    return render(request, 'blogs/post.html', {'post':post, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form})
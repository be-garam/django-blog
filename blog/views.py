from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import include
from django.utils import timezone

from .models import Post, Comment

def post_list(request):
    posts = Post.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()  # get all comments for this post
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})
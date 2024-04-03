from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import include
from django.utils import timezone

from .models import Post

def post_list(request):
    posts = Post.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    return render(request, 'blog/post_list.html', {'posts': posts})

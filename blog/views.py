from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import include
from django.utils import timezone
from django.views import generic

from .models import Post, Comment
from .forms import CommentForm

class PostListView(generic.ListView):
    model = Post
    ordering = ['-date_posted']
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

class AboutView(generic.TemplateView):
    template_name = 'blog/about.html'

class ContactView(generic.TemplateView):
    template_name = 'blog/contact.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
        return redirect('blog:post_detail', pk=self.object.pk)
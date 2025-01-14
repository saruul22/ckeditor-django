from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post, Article

# Create your views here.

def home_page_view(request):
    return HttpResponse("Hello, World!")


# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

# View single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'

# Create new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'pages/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

# Update post
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'pages/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

# Delete post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'pages/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
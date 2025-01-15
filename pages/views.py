from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post, Article

# Basic view
def home_page_view(request):
    return HttpResponse("Hello, World!")

# Django Class-Based Views for template rendering
class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'pages/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'pages/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'pages/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

# REST API Views
class PostAPIView(APIView):
    """API endpoints for Posts that allows CRUD operations"""
    
    def get(self, request, pk=None):
        if pk:
            post = get_object_or_404(Post, pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
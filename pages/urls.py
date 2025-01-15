from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views

from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, PostAPIView  # Make sure PostAPIView is imported
)

urlpatterns = [
    # Template-based views
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # API endpoints
    path('posts/', PostAPIView.as_view(), name='post-list-api'),
    path('posts/<int:pk>/', PostAPIView.as_view(), name='post-detail-api'),
    
]
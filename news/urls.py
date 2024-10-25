from django.urls import path

from home.apps import HomeConfig
from . import views

app_name = HomeConfig.name

urlpatterns = [
    path('posts/', views.PostsListView.as_view(), name='posts'),
    path('posts/create/', views.AddPostCreateView.as_view(), name='addpost'),
    path('posts/update/<slug:slug_id>/', views.UpdatePostView.as_view(), name='updatepost'),
    path('posts/delete/<slug:slug_id>/', views.DeletePostView.as_view(), name='deletepost'),
    path('posts/<slug:slug_id>/', views.PostDetailView.as_view(), name='post'),
]

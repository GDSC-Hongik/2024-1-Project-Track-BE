from django.urls import path

from . import views

urlpatterns = [
    # posts
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # profile
    path('users/<int:user_id>/', views.ProfileView.as_view(), name='profile'),
    path('users/<int:user_id>/posts/', views.UserPostListView.as_view(), name='user-post-list'),
    path('set-profile/', views.ProfileSetView.as_view(), name='profile-set'),
    path('edit-profile/', views.ProfileUpdateView.as_view(), name='profile-update'),
]

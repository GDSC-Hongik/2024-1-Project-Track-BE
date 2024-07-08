from django.urls import path

from . import views

urlpatterns = [
    # posts
    path('', views.IndexView.as_view(), name='index'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('posts/following/', views.FollowingPostListView.as_view(), name='following-post-list'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # profile
    path('users/<int:user_id>/', views.ProfileView.as_view(), name='profile'),
    path('users/<int:user_id>/posts/', views.UserPostListView.as_view(), name='user-post-list'),
    path('set-profile/', views.ProfileSetView.as_view(), name='profile-set'),
    path('edit-profile/', views.ProfileUpdateView.as_view(), name='profile-update'),

    # comment
    path('posts/<int:post_id>/comments/create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:comment_id>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:comment_id>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # like 
    path('like/<int:content_type_id>/<int:object_id>/', views.ProcessLikeView.as_view(), name='process-like'),

    # follow
    path('users/<int:user_id>/follow/', views.ProcessFollowView.as_view(), name='process-follow',),
]

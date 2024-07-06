from django.urls import path

from . import views

urlpatterns = [
    # review
    path('', views.IndexView.as_view(), name='index'),
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/following/', views.FollowingReviewListView.as_view(), name='following-review-list'),
    path('search/', views.SearchView.as_view(), name='search'), 
    path('reviews/<int:review_id>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/new/', views.ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:review_id>/edit/', views.ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:review_id>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),

    # profile
    path('users/<int:user_id>/', views.ProfileView.as_view(), name='profile'),
    path('users/<int:user_id>/reviews/', views.UserReviewListView.as_view(), name='user-review-list'),
    path('set-profile/', views.ProfileSetView.as_view(), name='profile-set'),
    path('edit-profile/', views.ProfileUpdateView.as_view(), name='profile-update'),

    # comment
    path(
        'reviews/<int:review_id>/comments/create/',
        views.CommentCreateView.as_view(),
        name='comment-create',
    ),
    path('comments/<int:comment_id>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:comment_id>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # like
    path(
        'like/<int:content_type_id>/<int:object_id>/',
        views.ProcessLikeView.as_view(),
        name='process-like'
    ),

    # follow
    path(
        'users/<int:user_id>/follow/',
        views.ProcessFollowView.as_view(),
        name='process-follow'
    ),
    path('users/<int:user_id>/following/', views.FollowingListView.as_view(), name='following-list'),
    path('users/<int:user_id>/followers/', views.FollowerListView.as_view(), name='follower-list'),

]

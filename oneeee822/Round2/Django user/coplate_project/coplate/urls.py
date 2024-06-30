from django.urls import path
from . import views

urlpatterns = [
    # review
    path("", views.IndexView.as_view(), name="index"),
    path("reviews/<int:review_id>/",
          views.ReviewDetailView.as_view(),
          name="review-detail",
    ),
    path("reviews/new/", views.ReviewCreateView.as_view(),name="review-create"),
    path("reviews/<int:review_id>/edit/", views.ReviewUpdateView.as_view(),name="review-update"),
    
    #profile urls
    path("users/<int:user_id>", views.ProfileView.as_View(), name="profile"),
    path(
        "users/<int:user_id>/reviews/",
        views.UserReviewListView.as_view(),
        name="user-review-list",
    ),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
    path("edit-profile/", views.ProfileUpdateView.as_view(), name="profile-update"),
]
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('posts/', views.post_list),
    # path('posts/new', views.post_create),
    # path('posts/<int:post_id>/', views.post_detail),
    # path('posts/<int:post_id>/edit', views.post_update),
    # path('posts/<int:post_id>/delete', views.post_delete),
]

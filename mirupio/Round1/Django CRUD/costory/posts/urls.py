from django.urls import path
from . import views

urlpatterns = [
	path('', views.IndexRedirectView.as_view(), name='index'),
	path('posts/', views.PostListView.as_view(), name='post-list'),
	path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
	path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
	path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
	path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]

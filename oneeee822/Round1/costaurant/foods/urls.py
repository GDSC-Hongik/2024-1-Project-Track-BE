from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index),
    path('menu/<int:pk>/', views.food_detail)
]

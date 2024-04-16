from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create-post/', views.create_post, name='create-post'),
    path('display-posts/', views.display_posts, name='display-posts'),
]

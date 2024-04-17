from django.urls import path
from . import views
from django.conf.urls import handler404


handler404 = 'app.views.custom_404'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('create-post/', views.create_post, name='create-post'),
    path('display-posts/', views.display_posts, name='display-posts'),
]

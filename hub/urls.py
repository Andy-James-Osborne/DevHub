from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('profile/<username>/', views.profile, name='profile'), 
    path('post_feed/', views.post_feed, name='post_feed'),  
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),  
    path('like_post/<int:pk>/', views.like_post, name='like_post'),  
    path('comment_view/<int:pk>/', views.comment_view, name='comment_view'),
    path("login/", views.login_user, name="login"),
     path("logout/", views.logout_user, name="logout"),
]

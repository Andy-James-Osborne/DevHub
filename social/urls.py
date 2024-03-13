from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("edit/<int:pk>/", views.post_detail, name="edit_detail"),
    path("delete/<int:pk>/", views.post_detail, name="delete_detail"),
    path("create_post/", views.create_post, name="create_post"),
    path("profile/", views.user_profile, name="profile"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
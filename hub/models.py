from django.db import models
from cloudinary.models import CloudinaryField


class User(models.Model):
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('profile_pictures', default='placeholder', blank=True)



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Replace with the appropriate on_delete behavior
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')  # Replace with the appropriate on_delete behavior
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')  # Replace with the appropriate on_delete behavior
    date_followed = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('follower', 'following'),)  # Ensures a user can only follow another user once




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Replace with the appropriate on_delete behavior
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Replace with the appropriate on_delete behavior
    like_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'post'),)  # Ensures a user can only like a post once



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Replace with the appropriate on_delete behavior
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Replace with the appropriate on_delete behavior
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


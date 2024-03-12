from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

User = get_user_model() #Get current user


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profliepic = models.ImageField(upload_to='profile_images', default='5907.jpg')
    profile_picture = CloudinaryField('profile_pictures', default='placeholder', blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
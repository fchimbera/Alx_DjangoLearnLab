from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from PIL import Image

# This is a custom user model that extends the AbstractUser class from Django's auth module.
# It adds additional fields for user profiles, such as bio and profile picture.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username

# Create your models here.

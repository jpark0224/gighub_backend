from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ExtendedUser(AbstractUser):
    display_name = models.CharField(max_length=30, unique=True)
    profile_picture = models.URLField(max_length=200)
    is_artist = models.BooleanField(default=False)

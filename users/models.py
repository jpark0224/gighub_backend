from django.db import models
from django.contrib.auth.models import AbstractUser

# make an email field required
from django.contrib.auth.models import User
User._meta.get_field('email').blank = False


class ExtendedUser(AbstractUser):
    display_name = models.CharField(max_length=30, unique=True)
    profile_picture = models.ImageField(upload_to='private/profile_pictures', default='public/blank-profile-picture.jpeg', blank=True)
    is_artist = models.BooleanField(default=False)

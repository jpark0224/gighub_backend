from django.db import models
from django.contrib.auth.models import AbstractUser

# make an email field required
from django.contrib.auth.models import User
User._meta.get_field('email').blank = False


class ExtendedUser(AbstractUser):
    display_name = models.CharField(max_length=30, unique=True)
    profile_picture = models.URLField(max_length=200, null=True, blank=True)
    is_artist = models.BooleanField(default=False)

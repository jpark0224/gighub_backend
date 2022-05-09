from django.db import models
from users.models import ExtendedUser

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_lengh=50, unique=True)
    profile_picture = models.URLField(max_length=200)

    users = models.ManyToManyField(
        ExtendedUser, blank=True, related_name="users_following_group")

    def __str__(self):
        return f"{self.name}"

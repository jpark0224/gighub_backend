from django.db import models
from users.models import ExtendedUser

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    profile_picture = models.URLField(max_length=200, null=True, blank=True)

    users = models.ManyToManyField(
        ExtendedUser, blank=True, related_name="users_following_group")

    created_by = models.ForeignKey(ExtendedUser,
                                   on_delete=models.SET_NULL, null=True, related_name="created_user")

    def __str__(self):
        return f"{self.name}"

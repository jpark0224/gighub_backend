from django.db import models

from groups.models import Group
from users.models import ExtendedUser

# Create your models here.


class Post(models.Model):
    contents = models.TextField()
    picture = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    group = models.ForeignKey(
        Group, null=True, blank=True, on_delete=models.CASCADE, related_name="posted_group")
    user = models.ForeignKey(ExtendedUser,
                             on_delete=models.CASCADE, related_name="posted_user")

    liked_user = models.ForeignKey(ExtendedUser, default='',
                                   on_delete=models.CASCADE, related_name="post_liked_user")
    bookmarked_user = models.ForeignKey(ExtendedUser, default='',
                                        on_delete=models.CASCADE, related_name="bookmarked_user")

    def __str__(self):
        return f"{self.contents}"

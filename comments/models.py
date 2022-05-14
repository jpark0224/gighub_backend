from django.db import models

from groups.models import Group
from posts.models import Post
from users.models import ExtendedUser

# Create your models here.


class Comment(models.Model):
    contents = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(ExtendedUser,
                                   on_delete=models.SET_NULL, null=True, related_name="commented_user")

    post = models.ForeignKey(
        Post, null=True, on_delete=models.CASCADE, related_name="commented_post")

    liked_user = models.ManyToManyField(ExtendedUser,
                                        blank=True, default=None, related_name="comment_liked")

    def __str__(self):
        return f"{self.contents}"

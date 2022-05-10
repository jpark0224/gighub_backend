from django.db import models

from groups.models import Group
from posts.models import Post
from users.models import ExtendedUser

# Create your models here.


class Comment(models.Model):
    contents = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    group = models.ForeignKey(
        Group, null=True, blank=True, on_delete=models.CASCADE, related_name="commented_group")
    post = models.ForeignKey(
        Post, null=True, blank=True, on_delete=models.CASCADE, related_name="commented_post")
    user = models.ForeignKey(ExtendedUser,
                             on_delete=models.CASCADE, related_name="commented_user")
    liked_user = models.ForeignKey(ExtendedUser, default='',
                                   on_delete=models.CASCADE, related_name="comment_liked_user")

    def __str__(self):
        return f"{self.contents}"

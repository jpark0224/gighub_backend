from django.db import models

from groups.models import Group
from users.models import ExtendedUser

# Create your models here.


class Post(models.Model):
    contents = models.TextField()
    picture = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(ExtendedUser, null=True,
                                   on_delete=models.CASCADE, related_name="posts")
    # created_by_username = models.ForeignKey(ExtendedUser, null=True,
    #                                         on_delete=models.CASCADE, related_name="posts_user")
    # created_by_profile_picture = models.ForeignKey(ExtendedUser, null=True,
    #                                                on_delete=models.CASCADE, related_name="posts_profile_picture")
    # created_by_is_artist = models.ForeignKey(ExtendedUser, null=True,
    #                                          on_delete=models.CASCADE, related_name="posts_is_artist")

    group = models.ForeignKey(
        Group, null=True, on_delete=models.CASCADE, related_name="posts")

    liked_user = models.ManyToManyField(ExtendedUser,
                                        blank=True, default=None, related_name="liked_posts")
    bookmarked_user = models.ManyToManyField(ExtendedUser,
                                             blank=True, default=None, related_name="bookmarked_posts")

    def __str__(self):
        return f"{self.contents}"

from rest_framework import serializers
from django.contrib.auth.models import User

from groups.models import Group
from posts.models import Post
from users.models import ExtendedUser


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ("email", "display_name", "is_artist", "profile_picture", )


class PostSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    user = UserSerializer()

    class Meta:
        model = Post
        fields = "__all__"

    # def validate(self, attrs):
    #     # add some custom validation

    #     # 1. get the currently logged in user
    #     # 2. check that the user is premium

    #     request = self.context.get("request")
    #     if request and hasattr(request, "user"):
    #         if not request.user.is_premium:
    #             raise serializers.ValidationError({
    #                 "is_premium": "Only premium users can create and update books."
    #             })

    #     return attrs

    # data is already validated
    def create(self, data):
        user_data = data.pop("user")
        group_data = data.pop("group")

        post = Post(
            contents=data["contents"],
            picture=data["picture"],
        )

        if user_data:
            user, _created = ExtendedUser.objects.get_or_create(**user_data)
            post.user = user

        if group_data:
            group, _created = Group.objects.get_or_create(**group_data)
            post.group = group

        # set the creator of a post to be the currently logged-in user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            post.user = request.user

        # Need to save to get the id
        post.save()

        # render to the api
        return post

    def update(self, post, data):
        user_data = data.pop("user")
        group_data = data.pop("group")

        post.contents = data.get("contents", post.contents)
        post.picture = data.get("rating", post.picture)

        if user_data:
            user, _created = ExtendedUser.objects.get_or_create(**user_data)
            post.user = user

        if group_data:
            group, _created = Group.objects.get_or_create(**group_data)
            post.group = group

        # set the creator of a post to be the currently logged-in user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            post.user = request.user

        # Need to save to get the id
        post.save()

        # render to the api
        return post

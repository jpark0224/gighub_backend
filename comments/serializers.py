from rest_framework import serializers
from django.contrib.auth.models import User
from comments.models import Comment

from groups.models import Group
from posts.models import Post
from users.models import ExtendedUser


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ("email", "display_name", "is_artist", "profile_picture", )


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    liked_user = UserSerializer(many=True, read_only=True)
    # post = serializers.PrimaryKeyRelatedField(read_only=True)
    post_id = serializers.IntegerField(write_only=True)
    # post = PostSerializer()

    class Meta:
        model = Comment
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
        post_id = data.pop("post_id")
        # liked_user_data = data.pop("liked_user")

        comment = Comment(
            contents=data["contents"],
        )

        # if liked_user_data:
        #     liked_user, _created = ExtendedUser.objects.get_or_create(
        #         **liked_user_data)
        #     post.liked_user = liked_user

        if post_id:
            post = Post.objects.get(id=post_id)
            comment.post = post

        # set the creator of a comment to be the currently logged-in user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            comment.created_by = request.user

        # Need to save to get the id
        comment.save()

        # render to the api
        return comment

    def update(self, comment, data):
        post_data = data.pop("post")
        created_by_data = data.pop("created_by")
        liked_user_data = data.pop("liked_user")
        group_data = data.pop("group")

        comment.contents = data.get("contents", comment.contents)

        if liked_user_data:
            liked_user, _created = ExtendedUser.objects.get_or_create(
                **liked_user_data)
            post.liked_user = liked_user

        if post_data:
            post, _created = Post.objects.get_or_create(**post_data)
            comment.post = post

        if created_by_data:
            user, _created = ExtendedUser.objects.get_or_create(
                **created_by_data)
            comment.user = user

        if group_data:
            group, _created = Group.objects.get_or_create(**group_data)
            comment.group = group

        # set the creator of a comment to be the currently logged-in user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            comment.created_by = request.user

        # Need to save to get the id
        comment.save()

        # render to the api
        return comment

from rest_framework import serializers
from django.contrib.auth.models import User

from groups.models import Group
from posts.models import Post
from users.models import ExtendedUser
from comments.models import Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ("display_name", "username", "profile_picture", "is_artist", )


class CommentsSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    # created_by = serializers.StringRelatedField()
    created_by = UserSerializer(read_only=True)
    liked_user = UserSerializer(many=True, read_only=True)
    # bookmarked_user = UserSerializer(read_only=True)
    comments_on_post = CommentsSerializer(
        many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    # def validate(self, attrs):
    #     # add some custom validation

    #     # get the currently logged in user

    #     request = self.context.get("request")
    #     if request and hasattr(request, "user"):
    #         if not request.user.is_premium:
    #             raise serializers.ValidationError({
    #                 "is_premium": "Only premium users can create and update books."
    #             })

    #     return attrs

    # data is already validated
    def create(self, data):
        group_data = data.pop("group")
        # created_by_data = data.pop("created_by")

        post = Post(
            contents=data["contents"],
            picture=data["picture"],
        )

        if group_data:
            group, _created = Group.objects.get_or_create(**group_data)
            post.group = group

        # set the creator of a post to be the currently logged-in user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            post.created_by = request.user
            # post.created_by_username = request.user.username

        # Need to save to get the id
        post.save()

        # render to the api
        return post

    def update(self, post, data):
        # set the creator of a post to be the currently logged-in user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            post.user = request.user

        liked_user_data = data.pop("liked_user", [])
        print(liked_user_data)
        # bookmarked_user_data = data.pop("bookmarked_user")

        post.contents = data.get("contents", post.contents)
        post.picture = data.get("picture", post.picture)

        if liked_user_data:
            liked_user, _created = ExtendedUser.objects.get_or_create(
                **liked_user_data)
            post.liked_user = request.user

        # if bookmarked_user_data:
        #     bookmarked_user, _created = ExtendedUser.objects.get_or_create(
        #         **user_data)
        #     post.bookmarked_user = bookmarked_user

        # if user_data:
        #     user, _created = ExtendedUser.objects.get(**user_data)
        #     post.user = user

        # Need to save to get the id
        post.save()

        # render to the api
        return post

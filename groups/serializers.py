from rest_framework import serializers
from django.contrib.auth.models import User
from groups.models import Group

from users.models import ExtendedUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ("display_name", "is_artist", "profile_picture", )


class GroupSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    users = UserSerializer(many=True)
    # posts = PostSerializer()

    class Meta:
        model = Group
        fields = "__all__"

# write a validate function for only admins to be able to create groups

    # data is already validated
    def create(self, data):
        created_by_data = data.pop("created_by")
        user_data = data.pop("users")
        # post_data = data.pop("posts")

        group = Group(
            name=data["name"],
            profile_picture=data["profile_picture"],)

        # many to many
        if user_data:
            for user in user_data:
                newUser, _created = ExtendedUser.objects.get_or_create(
                    **user)
                group.users.add(newUser)

        if created_by_data:
            created_by, _created = ExtendedUser.objects.get_or_create(
                **created_by_data)
            group.created_by = created_by

        group.save()

        # render to the api
        return group

    def update(self, group, data):
        created_by_data = data.pop("created_by")
        user_data = data.pop("users")
        # post_data = data.pop("posts")

        group.name = data.get("name", group.name)
        group.profile_picture = data.get(
            "profile_picture", group.profile_picture)

        if user_data:
            for user in user_data:
                newUser, _created = ExtendedUser.objects.get_or_create(
                    **user)
                group.users.add(newUser)

        if created_by_data:
            created_by, _created = ExtendedUser.objects.get_or_create(
                **user_data)
            group.created_by = created_by

        group.save()

        # render to the api
        return group

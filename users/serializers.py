from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from users.models import ExtendedUser
from django.core.files.base import ContentFile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ('username', 'display_name', 'password',
                  'password_repeat', 'email', 'profile_picture', 'is_artist')
        extra_kwargs = {
            'display_name': {'required': True}
        }

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=ExtendedUser.objects.all())]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    password_repeat = serializers.CharField(write_only=True, required=True)

    def validate(self, attributes):
        if attributes["password"] != attributes["password_repeat"]:
            raise serializers.ValidationError(
                {"password": "Password fields don't match."}
            )
        return attributes

    def create(self, data):

        try:
            user = ExtendedUser.objects.create(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password'],
                email=data['email'],
                profile_picture=data['profile_picture']
        )
        except KeyError:
            user = ExtendedUser.objects.create(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password'],
                email=data['email'],
        )
        
        user.set_password(data['password'])

        user.save()

        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ('display_name', 
                  'profile_picture')

    def update(self, user, data):
        user_profile = ExtendedUser.objects.get(username=user)

        if 'display_name' in data and 'profile_picture' in data:
            display_name_data = data.pop('display_name')
            profile_picture_data = data.pop('profile_picture')
            user.display_name = display_name_data
            user.profile_picture = profile_picture_data

        elif 'display_name' in data:
            display_name_data = data.pop('display_name')
            user.display_name = display_name_data
            user.profile_picture = user_profile.profile_picture

        elif 'profile_picture' in data:
            profile_picture_data = data.pop('profile_picture')
            user.profile_picture = profile_picture_data
            user.display_name = user_profile.display_name
        
        else:
            user.display_name = user_profile.display_name
            user.profile_picture = user_profile.profile_picture

        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = '__all__'

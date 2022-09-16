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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = '__all__'

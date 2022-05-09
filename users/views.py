from rest_framework import generics
from rest_framework.response import Response

from users.models import ExtendedUser
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):

    permission_classes = [AllowAny]
    queryset = ExtendedUser.objects.all()
    serializer_class = RegisterSerializer

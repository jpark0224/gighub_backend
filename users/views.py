from rest_framework import generics
from rest_framework.response import Response

from users.models import ExtendedUser
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from backend.permissions import IsRequestingUserOrReadOnly

class RegisterView(generics.CreateAPIView):

    permission_classes = [AllowAny]
    queryset = ExtendedUser.objects.all()
    serializer_class = RegisterSerializer

class RegisterDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRequestingUserOrReadOnly]
    queryset = ExtendedUser.objects.all()
    serializer_class = RegisterSerializer

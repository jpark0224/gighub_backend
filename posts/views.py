from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.permissions import IsCreatorOrReadOnly
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            queryset = Post.objects.order_by("-created_at")
            group = self.request.GET.get("group", None)
            if group is not None:
                queryset = queryset.filter(group_id=group)
            return queryset

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCreatorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


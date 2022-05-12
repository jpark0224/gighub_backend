from backend.permissions import IsCreatorOrReadOnly, IsGroupEditor
from groups.models import Group
from groups.serializers import GroupSerializer
from rest_framework import generics


# Create your views here.
class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsGroupEditor]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

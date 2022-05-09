from django.urls import path
from groups.views import GroupDetailView, GroupListView

urlpatterns = [
    path("", GroupListView.as_view(), name="creator-list"),
    path("<int:pk>", GroupDetailView.as_view(), name="creator-view"),
]

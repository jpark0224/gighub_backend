from django.urls import path
from comments.views import CommentDetailView, CommentListView


urlpatterns = [
    path("", CommentListView.as_view(), name="creator-list"),
    path("<int:pk>", CommentDetailView.as_view(), name="creator-view"),
]

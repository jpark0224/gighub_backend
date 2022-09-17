from django.urls import path, include
from .views import RegisterView, RegisterDetailView
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('register', RegisterView.as_view()),
    path("<int:pk>", RegisterDetailView.as_view()),
]


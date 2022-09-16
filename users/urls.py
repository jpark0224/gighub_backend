from django.urls import path, include
from .views import RegisterView
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('register', RegisterView.as_view()),
]


from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models


from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change) -> None:
        obj.user = request.user
        return super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Post, PostAdmin)

# Generated by Django 4.0.4 on 2022-05-13 12:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_remove_post_bookmarked_user_post_bookmarked_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookmarked_user',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarked_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='liked_user',
            field=models.ManyToManyField(blank=True, default=None, related_name='post_liked_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
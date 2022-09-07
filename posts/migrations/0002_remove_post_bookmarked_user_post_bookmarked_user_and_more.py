# Generated by Django 4.0.4 on 2022-05-13 12:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bookmarked_user',
        ),
        migrations.AddField(
            model_name='post',
            name='bookmarked_user',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='bookmarked_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='liked_user',
        ),
        migrations.AddField(
            model_name='post',
            name='liked_user',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='post_liked_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
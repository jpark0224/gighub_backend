# Generated by Django 4.0.4 on 2022-05-14 08:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0003_comment_liked_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='bookmarked_user',
            field=models.ManyToManyField(blank=True, default=None, related_name='comment_bookmarked', to=settings.AUTH_USER_MODEL),
        ),
    ]

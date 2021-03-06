# Generated by Django 4.0.4 on 2022-05-14 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0004_rename_creator_group_created_by'),
        ('posts', '0008_alter_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookmarked_user',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='groups.group'),
        ),
        migrations.AlterField(
            model_name='post',
            name='liked_user',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-12 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0002_alter_group_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
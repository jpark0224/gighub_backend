# Generated by Django 4.0.4 on 2022-05-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]

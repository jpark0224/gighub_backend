# Generated by Django 4.1.1 on 2022-09-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_extendeduser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='profile_picture',
            field=models.ImageField(default='blank-profile-picture.jpeg', upload_to='profile_pictures'),
        ),
    ]
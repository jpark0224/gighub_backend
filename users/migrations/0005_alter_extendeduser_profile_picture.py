# Generated by Django 4.1.1 on 2022-09-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_extendeduser_is_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='profile_picture',
            field=models.ImageField(default='blank-profile.picture.jpeg', upload_to='profile_pictures'),
        ),
    ]
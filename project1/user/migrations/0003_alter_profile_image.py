# Generated by Django 4.2.4 on 2023-11-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="profile_images/profilepic.jpg", upload_to="profile_images"
            ),
        ),
    ]

# Generated by Django 4.0.2 on 2022-04-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                default="blank-profile-picture.webp",
                null=True,
                upload_to="",
            ),
        ),
    ]
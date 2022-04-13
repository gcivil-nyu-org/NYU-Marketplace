# Generated by Django 4.0.2 on 2022-04-12 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0008_alter_interest_cust_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="option",
            field=models.IntegerField(
                choices=[
                    ("1", "Inappropriate post content"),
                    ("2", "Post item is unavailable anymore"),
                    ("3", "Cannot reach out to post owner"),
                    ("4", "Other"),
                ],
                default=4,
                max_length=10,
            ),
        ),
    ]
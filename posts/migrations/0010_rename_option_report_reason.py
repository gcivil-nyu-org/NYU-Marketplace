# Generated by Django 4.0.2 on 2022-04-12 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0009_report_option"),
    ]

    operations = [
        migrations.RenameField(
            model_name="report",
            old_name="option",
            new_name="reason",
        ),
    ]

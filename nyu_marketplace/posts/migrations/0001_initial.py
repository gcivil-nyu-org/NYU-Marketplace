# Generated by Django 4.0.2 on 2022-03-01 06:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')])),
                ('description', models.TextField(max_length=400, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('option', models.CharField(choices=[('sell', 'Sell'), ('rent', 'Rent'), ('exchange', 'Exchange')], default='Rent', max_length=10)),
                ('category', models.CharField(choices=[('textbook', 'Textbook'), ('tech', 'Tech'), ('sport', 'Sport')], default='Textbook', max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('location', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')])),
                ('picture', models.BinaryField(editable=True, null=True)),
                ('content_type', models.CharField(help_text='The MIMEType of the file', max_length=256, null=True)),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-04-27 14:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Name must be at least 2 characters long')])),
                ('description', models.TextField(max_length=400, validators=[django.core.validators.MinLengthValidator(2, 'Description must be at least 2 characters long')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('option', models.CharField(choices=[('sell', 'Sell'), ('rent', 'Rent'), ('exchange', 'Exchange')], default='Rent', max_length=10)),
                ('category', models.CharField(choices=[('textbook', 'Textbook'), ('tech', 'Tech'), ('sport', 'Sport'), ('furniture', 'Furniture'), ('other', 'Other')], default='Textbook', max_length=10)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('location', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Location must be greater than 2 characters long')])),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('report_count', models.PositiveIntegerField(default=0)),
                ('interested_count', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.IntegerField(choices=[('1', 'Inappropriate post content'), ('2', 'Post item is unavailable anymore'), ('3', 'Cannot reach out to post owner'), ('4', 'Other')], default=4, max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('post', 'reported_by')},
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_message', models.TextField(max_length=400, null=True, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')])),
                ('interested_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
            options={
                'unique_together': {('post', 'interested_user')},
            },
        ),
    ]

from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser



class Post(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    description = models.TextField()
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    option = (
        ('rent', "Rent"),
        ('sell', "Sell"),
        ('exchange', "Exchange"),
    )
    option = models.CharField(max_length=10, choices=option)


    # Picture

    # Shows up in the admin list
    def __str__(self):
        return self.name
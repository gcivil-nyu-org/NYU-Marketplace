from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(
        null=True, editable=True, blank=True, default="blank-profile-picture.webp"
    )

    genders = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    gender = models.CharField(max_length=10, choices=genders, default="")

    schools = (
        ("tandon", "Tandon School of Engineering"),
        ("tish", "Tisch School of Arts"),
        ("stern", "Stern School of Business"),
    )
    school = models.CharField(max_length=10, choices=schools, default="")
    address = models.CharField(max_length=50, default="")

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profile_pic", "gender", "school", "address")
        widgets = {
            "gender": forms.RadioSelect(
                attrs={"class": "form-check-inline", "id": "inputOption"}
            ),
            "school": forms.Select(
                attrs={"class": "form-select col-sm-9", "id": "inputCategory"}
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "itemLocation",
                    "id": "inputItemLocation",
                }
            ),
        }

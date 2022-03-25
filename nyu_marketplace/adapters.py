from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from django.contrib.auth.models import User


class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        domain = email.split("@")[1]
        emails = User.objects.values_list("email", flat=True)
        if domain != "nyu.edu":
            raise ValidationError("You are not using NYU email account.")
        if email in emails:
            raise ValidationError(
                "A user is already registered with this e-mail address."
            )
        return email


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        u = sociallogin.user
        return u.email.split("@")[1] == "nyu.edu"

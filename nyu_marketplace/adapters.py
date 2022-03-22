from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        u = sociallogin.user
        print(u.email)
        # Optionally, set as staff now as well.
        # This is useful if you are using this for the Django Admin login.
        # Be careful with the staff setting, as some providers don't verify
        # email address, so that could be considered a security flaw.
        # u.is_staff = u.email.split('@')[1] == "customdomain.com"
        return u.email.split("@")[1] == "nyu.edu"

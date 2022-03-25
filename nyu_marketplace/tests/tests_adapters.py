from allauth.tests import TestCase
from django.test.utils import override_settings
from allauth.utils import get_user_model
from allauth.account.models import (
    EmailAddress,
    EmailConfirmation,
    EmailConfirmationHMAC,
)
from django.urls import reverse
from django.core import mail, validators

class AccountTests(TestCase):
    @override_settings(
        ACCOUNT_LOGIN_ATTEMPTS_LIMIT=1,
    )
    def test_login_using_unverified_email_address_is_prohibited(self):
        user = get_user_model().objects.create(
            username="john", email="john@example.org", is_active=True
        )
        user.set_password("doe")
        user.save()

        EmailAddress.objects.create(
            user=user, email="john@example.org", primary=True, verified=True
        )
        EmailAddress.objects.create(
            user=user, email="john@example.com", primary=True, verified=False
        )

        resp = self.client.post(
            reverse("account_login"), {"login": "john@example.com", "password": "doe"}
        )
        self.assertRedirects(
            resp,
            reverse("account_email_verification_sent"),
            fetch_redirect_response=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        assert mail.outbox[0].to == ["john@example.com"]

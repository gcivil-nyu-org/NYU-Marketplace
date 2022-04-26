from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase


class TestViews(TestCase):
    def setUp(self):
        self.poster = get_user_model().objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )

    def test_price_over_limit(self):
        login = self.client.login(email="test@example.com", password="12test12")
        self.assertEquals(login, True)
        response = self.client.post(
            "/posts/create/",
            {
                "name": "macbook pro",
                "description=": "used macbook pro",
                "option": "exchange",
                "category": "tech",
                "price": "1000000000",
                "location": "stern",
                "user": "self.poster",
                "picture": "https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "error")
        self.assertRaises(ValidationError)

    def test_price_under_limit(self):
        login = self.client.login(email="test@example.com", password="12test12")
        self.assertEquals(login, True)
        response2 = self.client.post(
            "/posts/create/",
            {
                "name": "macbook ",
                "description=": "used macbook pro",
                "option": "exchange",
                "category": "tech",
                "price": "1000",
                "location": "stern",
                "user": "self.poster",
                "picture": "https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
            },
        )
        self.assertEqual(response2.status_code, 200)
        self.assertNotContains(response2, "Price can not be larger than 1000000!")

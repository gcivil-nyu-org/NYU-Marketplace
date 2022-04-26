from django.contrib.auth import get_user_model
from django.test import TestCase
from io import BytesIO
from PIL import Image
from django.core.files.base import File


class TestViews(TestCase):
    def setUp(self):
        self.poster = get_user_model().objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )

    @staticmethod
    def get_image_file(name, ext="png", size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def test_price_over_limit(self):
        login = self.client.login(email="test@example.com", password="12test12")
        self.assertEquals(login, True)
        image1 = self.get_image_file("image.png")
        response = self.client.post(
            "/posts/create/",
            {
                "name": "macbook pro",
                "description": "used macbook pro",
                "option": "rent",
                "category": "tech",
                "price": 1000000000,
                "location": "stern",
                "picture": image1,
                "user": "self.poster",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "error")
        self.assertContains(response, "Price can not be larger than 1000000!")

    def test_price_under_limit(self):
        login = self.client.login(email="test@example.com", password="12test12")
        self.assertEquals(login, True)
        image1 = self.get_image_file("image.png")
        response = self.client.post(
            "/posts/create/",
            {
                "name": "macbook pro",
                "description": "used macbook pro",
                "option": "rent",
                "category": "tech",
                "price": 10000,
                "location": "stern",
                "picture": image1,
                "user": "self.poster",
            },
        )
        self.assertEqual(response.status_code, 302)

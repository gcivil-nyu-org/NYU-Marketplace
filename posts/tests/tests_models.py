from django.test import TestCase
from posts.models import Post


class TestModels(TestCase):
    def test_post(self):
        post = Post.objects.create(
            name="algorithm textbook",
            description="used testbook for cs6033",
            option="sell",
            category="textbook",
            price=5,
            location="tendon",
        )

        self.assertEquals(post.name, "algorithm textbook")
        self.assertEquals(post.description, "used testbook for cs6033")
        self.assertEquals(post.option, "sell")
        self.assertEquals(post.category, "textbook")
        self.assertEquals(post.price, 5)
        self.assertEquals(post.location, "tendon")

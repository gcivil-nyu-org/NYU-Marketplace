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

        post2 = Post.objects.create(
            name="macbook pro",
            description="used macbook pro",
            option="exchange",
            category="tech",
            price=50,
            location="stern",
        )

        post3 = Post.objects.create(
            name="ski board",
            description="head ski board",
            option="rent",
            category="sport",
            price=30,
            location="brooklyn",
        )

        self.assertEquals(post.name, "algorithm textbook")
        self.assertEquals(post.description, "used testbook for cs6033")
        self.assertEquals(post.option, "sell")
        self.assertEquals(post.category, "textbook")
        self.assertEquals(post.price, 5)
        self.assertEquals(post.location, "tendon")

        self.assertEquals(post2.name, "macbook pro")
        self.assertEquals(post2.description, "used macbook pro")
        self.assertEquals(post2.option, "exchange")
        self.assertEquals(post2.category, "tech")
        self.assertEquals(post2.price, 50)
        self.assertEquals(post2.location, "stern")

        self.assertEquals(post3.name, "ski board")
        self.assertEquals(post3.description, "head ski board")
        self.assertEquals(post3.option, "rent")
        self.assertEquals(post3.category, "sport")
        self.assertEquals(post3.price, 30)
        self.assertEquals(post3.location, "brooklyn")

from django import forms
from django.core.exceptions import ValidationError

from posts.models import Post
from posts import forms


def test_price_over_limit(self):
    instance = Post.objects.create(
        name="macbook pro",
        description="used macbook pro",
        option="exchange",
        category="tech",
        price=100000000,
        location="stern",
        user=self.poster,
        picture="https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
    )
    self.assertRaises(ValidationError, instance.clean)


def test_price_under_limit(self):
    instance = Post.objects.create(
        name="macbook pro",
        description="used macbook pro",
        option="exchange",
        category="tech",
        price=100.00,
        location="stern",
        user=self.poster,
        picture="https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
    )
    self.assertEquals(instance, instance.clean)

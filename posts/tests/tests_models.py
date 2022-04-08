from django.contrib.auth import get_user_model
from django.test import TestCase
from posts.models import Post, Report, Interest


class TestModels(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )
        self.reporter = get_user_model().objects.create_user(
            username="reporter", password="12test12", email="reporter@example.com"
        )
        self.interester = get_user_model().objects.create_user(
            username="interester", password="12test12", email="interester@example.com"
        )
        self.post = Post.objects.create(
            name="algorithm textbook",
            description="used testbook for cs6033",
            option="sell",
            category="textbook",
            price=5,
            location="tendon",
            user=self.user,
        )

    def test_post(self):

        post2 = Post.objects.create(
            name="macbook pro",
            description="used macbook pro",
            option="exchange",
            category="tech",
            price=50,
            location="stern",
            user=self.user,
        )

        post3 = Post.objects.create(
            name="ski board",
            description="head ski board",
            option="rent",
            category="sport",
            price=30,
            location="brooklyn",
            user=self.user,
        )

        self.assertEquals(self.post.name, "algorithm textbook")
        self.assertEquals(self.post.description, "used testbook for cs6033")
        self.assertEquals(self.post.option, "sell")
        self.assertEquals(self.post.category, "textbook")
        self.assertEquals(self.post.price, 5)
        self.assertEquals(self.post.location, "tendon")
        self.assertEquals(self.post.user.username, "test")
        self.assertEquals(self.post.user.username, "test")
        self.assertEqual(str(self.post), self.post.name)

        self.assertEquals(post2.name, "macbook pro")
        self.assertEquals(post2.description, "used macbook pro")
        self.assertEquals(post2.option, "exchange")
        self.assertEquals(post2.category, "tech")
        self.assertEquals(post2.price, 50)
        self.assertEquals(post2.location, "stern")
        self.assertEquals(post2.user.username, "test")
        self.assertEqual(str(post2), post2.name)

        self.assertEquals(post3.name, "ski board")
        self.assertEquals(post3.description, "head ski board")
        self.assertEquals(post3.option, "rent")
        self.assertEquals(post3.category, "sport")
        self.assertEquals(post3.price, 30)
        self.assertEquals(post3.location, "brooklyn")
        self.assertEquals(post3.user.username, "test")
        self.assertEqual(str(post3), post3.name)

    def test_report(self):
        report = Report.objects.create(
            post=self.post,
            reported_by=self.reporter,
        )
        self.assertEquals(str(report.post), self.post.name)
        self.assertEquals(report.reported_by.username, self.reporter.username)

    def test_interest(self):
        interest = Interest.objects.create(
            post=self.post,
            interested_user=self.interester,
        )
        self.assertEquals(
            str(interest), f"{self.interester.username} interested in {self.post}"
        )
        self.assertEquals(str(interest.post), self.post.name)
        self.assertEquals(interest.interested_user.username, self.interester.username)

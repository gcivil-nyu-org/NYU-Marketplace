from django.contrib.auth import get_user_model
from django.test import TestCase, Client

# from posts.models import Post


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # self.client.login(username='testuser', password='12345')
        self.user = get_user_model().objects.create_user(
            username="user", password="12test12", email="user@nyu.edu",
        )
        self.poster = get_user_model().objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )
        # post = Post.objects.create(
        #     name="algorithm textbook",
        #     description="used testbook for cs6033",
        #     option="sell",
        #     category="textbook",
        #     price=5,
        #     location="tendon",
        #     user=self.poster,
        # )
        # post2 = Post.objects.create(
        #     name="macbook pro",
        #     description="used macbook pro",
        #     option="exchange",
        #     category="tech",
        #     price=50,
        #     location="stern",
        #     user=self.poster,
        # )

    def test_post_get(self):
        response = self.client.get("/posts/")
        self.assertEquals(response.status_code, 302)
        # login = self.client.force_login(self.user)
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        response2 = self.client.get("/posts/")
        self.assertEquals(response2.status_code, 200)


    def test_post_create_get(self):
        response = self.client.get("/posts/create/")
        self.assertEquals(response.status_code, 302)
        # login = self.client.force_login(self.user)
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        response2 = self.client.get("/posts/create/")
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, "posts/createpost.html")

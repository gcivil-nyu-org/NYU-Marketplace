from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory
from posts.models import Post


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.request_factory = RequestFactory()
        # self.client.login(username='testuser', password='12345')
        self.user = get_user_model().objects.create_user(
            username="user",
            password="12test12",
            email="user@nyu.edu",
        )
        self.admin = get_user_model().objects.create_superuser(
            username="admin",
            password="admintestadmin",
            email="admin@nyu.edu",
        )
        self.poster = get_user_model().objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )

        # post2 = Post.objects.create(
        #     name="macbook pro",
        #     description="used macbook pro",
        #     option="exchange",
        #     category="tech",
        #     price=50,
        #     location="stern",
        #     user=self.poster,
        # )

    def test_admin_cannot_not_create_post(self):
        response = self.client.get("/posts/create/")
        self.assertEquals(response.status_code, 302)
        login = self.client.login(email="admin@nyu.edu", password="admintestadmin")
        self.assertEquals(login, True)
        response2 = self.client.get("/posts/create/")
        self.assertEquals(response2.status_code, 403)
        response3 = self.client.post("/posts/create/")
        self.assertEquals(response3.status_code, 403)

    def test_post_get(self):
        response = self.client.get("/posts/")
        self.assertEquals(response.status_code, 302)
        # login = self.client.force_login(self.user)
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        response2 = self.client.get("/posts/")
        self.assertEquals(response2.status_code, 200)
        data = {"category": "tech", "option": "rent", "sort": "pricedesc"}
        response3 = self.client.get("/posts/", data)
        self.assertEquals(response3.status_code, 200)
        data2 = {"category": "tech", "option": "rent", "sort": "priceasc"}
        response4 = self.client.get("/posts/", data2)
        self.assertEquals(response4.status_code, 200)
        data3 = {"category": "tech", "option": "reported", "sort": "priceasc"}
        response5 = self.client.get("/posts/", data3)
        self.assertEquals(response5.status_code, 403)
        self.client.logout()
        self.assertEquals(login, True)
        login = self.client.login(email="admin@nyu.edu", password="admintestadmin")
        self.assertEquals(login, True)
        data4 = {"category": "tech", "option": "reported", "sort": "priceasc"}
        response6 = self.client.get("/posts/", data4)
        self.assertEquals(response6.status_code, 200)

    def test_post_create_get(self):
        response = self.client.get("/posts/create/")
        self.assertEquals(response.status_code, 302)
        # login = self.client.force_login(self.user)
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        response2 = self.client.get("/posts/create/")
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, "posts/createpost.html")

    def test_detail_view(self):
        response = self.client.get("/posts/detail/1")
        self.assertEquals(response.status_code, 302)
        self.client.logout()
        Post.objects.create(
            name="macbook pro",
            description="used macbook pro",
            option="exchange",
            category="tech",
            price=50,
            location="stern",
            user=self.poster,
            picture="https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
        )
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        response2 = self.client.get("/posts/detail/1")
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, "posts/detail.html")
        report = {"report": "report"}
        response3 = self.client.post("/posts/detail/1", report)
        self.assertEquals(response3.status_code, 302)
        cancel_report = {"cancel_report": "cancel_report"}
        response4 = self.client.post("/posts/detail/1", cancel_report)
        self.assertEquals(response4.status_code, 302)
        self.client.logout()
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        edit_denied = {"edit": "edit"}
        response9 = self.client.post("/posts/detail/1", edit_denied)
        self.assertEquals(response9.status_code, 403)
        interested = {"interested": "interested"}
        response5 = self.client.post("/posts/detail/1", interested)
        self.assertEquals(response5.status_code, 200)
        cancel_interested = {"cancel_interest": "cancel_interest"}
        response9 = self.client.post("/posts/detail/1", cancel_interested)
        self.assertEquals(response9.status_code, 200)
        self.client.logout()
        login = self.client.login(password="12test12", email="test@example.com")
        self.assertEquals(login, True)
        edit = {"edit": "edit"}
        response6 = self.client.post("/posts/detail/1", edit)
        self.assertEquals(response6.status_code, 302)
        delete = {"delete": "delete"}
        response7 = self.client.post("/posts/detail/1", delete)
        self.assertEquals(response7.status_code, 302)
        response8 = self.client.get("/posts/detail/1")
        self.assertEquals(response8.status_code, 404)

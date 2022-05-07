from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from users.models import Profile
from posts.models import Post, Interest


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="user",
            password="12test12",
            email="user@nyu.edu",
        )
        self.poster = get_user_model().objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )
        self.admin = get_user_model().objects.create_superuser(
            username="admin",
            password="admintestadmin",
            email="admin@nyu.edu",
        )

    def test_profile_get(self):
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        self.client.logout()
        self.assertEquals(login, True)
        login = self.client.login(email="admin@nyu.edu", password="admintestadmin")
        self.assertEquals(login, True)

    def test_profile_details_get(self):
        response = self.client.get("/profile/profile_detail/")
        self.assertEquals(response.status_code, 302)
        # login = self.client.force_login(self.user)
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        # Profile.objects.create(
        #     user=self.user,
        #     profile_pic="https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
        #     gender="male",
        #     school="tandon",
        #     address="6 Metrotech Center",
        # )
        response2 = self.client.get("/profile/profile_detail/")
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, "users/profile_detail.html")

    def test_profile_post(self):
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        response = self.client.post(
            "/profile/edit_profile/",
            {
                "user": "self.user",
                "profile_pic": "https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
                "gender": "female",
                "school": "tandon",
                "address": "6 Metrotech Center",
            },
        )
        profile1 = Profile.objects.get(id=1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(profile1.gender, "female")
        self.assertEquals(profile1.school, "tandon")
        self.assertEquals(profile1.address, "6 Metrotech Center")

    def test_user_info_get(self):
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
        post = Post.objects.get(id=1)
        post.interested_count += 1
        post.save()
        Interest.objects.create(
            post=post,
            interested_user=self.user,
            cust_message="interesting",
        )
        response = self.client.get(f"/profile/user_info/{self.user.id}")
        self.assertEquals(response.status_code, 302)
        login = self.client.login(email="user@nyu.edu", password="12test12")
        self.assertEquals(login, True)
        response = self.client.get(f"/profile/user_info/{self.user.id}")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile_detail.html")
        self.assertIsNotNone(response.context["user_interested_list"])
        self.assertEquals(len(response.context["user_interested_list"]), 1)
        self.client.logout()
        login = self.client.login(email="admin@nyu.edu", password="admintestadmin")
        self.assertEquals(login, True)
        response2 = self.client.get(f"/profile/user_info/{self.user.id}")
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, "users/user_info.html")

    def test_post_interest_detail(self):
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
        login = self.client.login(email="test@example.com", password="12test12")
        self.assertEquals(login, True)
        response = self.client.get("/profile/post_interest_detail/1")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/post_interest_detail.html")

    def test_about_us(self):
        response = self.client.get("/profile/about_us")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/about_us.html")

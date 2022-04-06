# from django.contrib.auth import get_user_model
# from django.test import TestCase, Client
# from users.models import Profile
#
#
# class TestViews(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = get_user_model().objects.create_user(
#             username="user",
#             password="12test12",
#             email="user@nyu.edu",
#         )
#         self.admin = get_user_model().objects.create_superuser(
#             username="admin",
#             password="admintestadmin",
#             email="admin@nyu.edu",
#         )
#
#     def test_profile_get(self):
#         response = self.client.get("/profile/")
#         self.assertEquals(response.status_code, 302)
#         # login = self.client.force_login(self.user)
#         login = self.client.login(email="user@nyu.edu", password="12test12")
#         self.assertEquals(login, True)
#         response2 = self.client.get("/profile/")
#         self.assertEquals(response2.status_code, 200)
#         self.client.logout()
#         self.assertEquals(login, True)
#         login = self.client.login(email="admin@nyu.edu", password="admintestadmin")
#         self.assertEquals(login, True)
#         response6 = self.client.get("/profile/")
#         self.assertEquals(response6.status_code, 200)
#
#     def test_profile_details_get(self):
#         response = self.client.get("/profile/profile_detail/")
#         self.assertEquals(response.status_code, 302)
#         # login = self.client.force_login(self.user)
#         login = self.client.login(email="user@nyu.edu", password="12test12")
#         self.assertEquals(login, True)
#         Profile.objects.create(
#             user=self.user,
#             profile_pic="https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
#             gender="male",
#             school="tandon",
#             address="6 Metrotech Center",
#         )
#         response2 = self.client.get("/profile/profile_detail/")
#         self.assertEquals(response2.status_code, 200)
#         self.assertTemplateUsed(response2, "users/profile_detail.html")
#
#     def test_profile_post(self):
#         login = self.client.login(email="user@nyu.edu", password="12test12")
#         self.assertEquals(login, True)
#         response = self.client.post(
#             "/profile/",
#             {
#                 "user": "self.user",
#                 "profile_pic": "https://nyu-marketplace-team1.s3.amazonaws.com/algo.jpg",
#                 "gender": "male",
#                 "school": "tandon",
#                 "address": "6 Metrotech Center",
#             },
#         )
#         profile1 = Profile.objects.get(id=1)
#         self.assertEquals(response.status_code, 302)
#         self.assertEquals(profile1.gender, "male")
#         self.assertEquals(profile1.school, "tandon")
#         self.assertEquals(profile1.address, "6 Metrotech Center")

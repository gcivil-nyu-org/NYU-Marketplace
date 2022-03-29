from django.contrib.auth import get_user_model
from django.test import TestCase
from users.models import Profile


class TestModels(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )
        self.user2 = get_user_model().objects.create_user(
            username="test2", password="12test12", email="test@example.com"
        )

    def test_post(self):
        profile1 = Profile.objects.create(
            user=self.user,
            gender="male",
            school="tandon",
            address="6 Metrotech Center",
        )

        profile2 = Profile.objects.create(
            user=self.user2,
            gender="female",
            school="stern",
            address="7 Metrotech Center",
        )

        self.assertEquals(profile1.gender, "male")
        self.assertEquals(profile1.school, "tandon")
        self.assertEquals(profile1.address, "6 Metrotech Center")
        self.assertEquals(profile1.user.username, "test")

        self.assertEquals(profile2.gender, "female")
        self.assertEquals(profile2.school, "stern")
        self.assertEquals(profile2.address, "7 Metrotech Center")
        self.assertEquals(profile2.user.username, "test2")

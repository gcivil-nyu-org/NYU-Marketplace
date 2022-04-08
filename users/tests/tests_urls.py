from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import profile_detail, user_info, edit_profile


class TestUrls(SimpleTestCase):
    def test_profile_detail_url_is_resolved(self):
        url = reverse("users:profile_detail")
        self.assertEquals(resolve(url).func, profile_detail)
        self.assertEquals(url, "/profile/profile_detail/")

    def test_user_info_url_is_resolved(self):
        url = reverse("users:user_info", args=['1'])
        self.assertEquals(resolve(url).func, user_info)
        self.assertEquals(url, "/profile/user_info/1")

    def test_user_edit_profile_is_resolved(self):
        url = reverse("users:edit_profile")
        self.assertEquals(resolve(url).func, edit_profile)
        self.assertEquals(url, "/profile/edit_profile/")

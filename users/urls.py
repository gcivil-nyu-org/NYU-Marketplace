from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.edit_profile, name="profile"),
    path("profile_detail/", views.profile_detail, name="profile_detail"),
    path("about_us", views.about_us, name="about_us"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_info/<int:user_id>", views.user_info, name="user_info"),
    path(
        "post_interest_detail/<int:post_id>",
        views.post_interest_detail,
        name="post_interest_detail",
    ),
]

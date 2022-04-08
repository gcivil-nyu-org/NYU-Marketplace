from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    # path("", views.profile, name="profile"),
    path("profile_detail/", views.profile_detail, name="profile_detail"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_info/<int:user_id>", views.user_info, name="user_info"),
]

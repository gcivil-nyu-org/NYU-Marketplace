from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.profile, name="profile"),
    path("profile_detail/", views.profile_detail, name="profile_detail"),
]

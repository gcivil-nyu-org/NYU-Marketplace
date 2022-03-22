from django.urls import path

from . import views


urlpatterns = [
    path("", views.index.as_view(), name="home"),
    path("profile/", views.profile, name="profile"),
    # path('createpost/', views.createpost, name='createpost'),
    path("post_picture/<int:pk>", views.stream_file, name="post-picture"),
    path("create/", views.postCreate.as_view(), name="post-create"),
    path("detail/<int:post_id>", views.detail, name="detail"),
]

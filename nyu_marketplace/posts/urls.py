from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    #path('createpost/', views.createpost, name='createpost'),

    path('create/', views.post_create, name='post-create'),
    
]
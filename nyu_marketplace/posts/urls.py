from django.urls import path

from . import views
from .views import post_create

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    #path('createpost/', views.createpost, name='createpost'),

    path('create/', post_create, name='post-create'),
    
]
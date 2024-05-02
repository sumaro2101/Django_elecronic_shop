from django.urls import path

from home.apps import HomeConfig
from . import views

app_name = HomeConfig.name

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact/', views.contact, name='contact'),
    path('user/', views.user, name='user'),
    path('auth/', views.auth, name='auth'),
]

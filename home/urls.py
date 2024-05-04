from django.urls import path

from home.apps import HomeConfig
from . import views

app_name = HomeConfig.name

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('user/', views.UserView.as_view(), name='user'),
    path('auth/', views.AuthView.as_view(), name='auth'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact/', views.contact, name='contact'),
    path('user/', views.user, name='user'),
    path('auth/', views.auth, name='auth'),
]

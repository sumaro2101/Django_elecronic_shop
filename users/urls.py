from django.urls import path

from users.apps import UsersConfig
from . import views

app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.AuthView.as_view(), name='login'),
    path('user/', views.UserView.as_view(), name='user'),
]
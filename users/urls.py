from django.urls import path

from users.apps import UsersConfig
from . import views
from django.contrib.auth.views import LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.AuthView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('regisration/', views.RegisterUser.as_view(), name='reg'),
    path('regisration/done/', views.DoneTemplateView.as_view(), name='done'),
    path('user/<slug:username>/', views.UserDetailView.as_view(), name='user'),
    path('user/<slug:username>/update/', views.UpdateProfileUser.as_view(), name='update'),
]
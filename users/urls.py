from django.urls import path

from users.apps import UsersConfig
from . import views
from django.contrib.auth.views import LogoutView

app_name = UsersConfig.name

urlpatterns = [
    #login - logout
    path('login/', views.AuthView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    #registration
    path('regisration/', views.RegisterUser.as_view(), name='reg'),
    path('regisration/done/', views.DoneTemplateView.as_view(), name='done'),
    
    #user
    path('user/<slug:username>/', views.UserDetailView.as_view(), name='user'),
    path('user/<slug:username>/update/', views.UpdateProfileUser.as_view(), name='update'),
    
    #password_change
    path('password_change/', views.UserChangePassword.as_view(), name='password_change'),
    path('password_change/done/', views.UserChangePasswordDone.as_view(), name='password_change_done'),
    
    #password_reset
    path('password_reset/', views.UserResetPassword.as_view(), name='password_reset'),
    path('password_reset/done/', views.UserResetPasswordDone.as_view(), name='password_reset_done'),
    path('password_reset/complete/', views.UserResetPasswordComplete.as_view(), name='password_reset_complete'),
    path('password_reset/<uidb64>/<token>/', views.UserResetPasswordConfirm.as_view(), name='password_reset_confirm'),
]
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views2 import SignUpView,UserUpdateView,MyLoginView

app_name = "accounts"

urlpatterns = [
    path('register/',SignUpView.as_view(),name="register"),
    path('login/',MyLoginView.as_view() ,name="loginUser"),
    path('logout/', auth_views.LogoutView.as_view(),name="logoutUser"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='includes/user/reset_password.html'),name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='includes/user/reset_password_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='includes/user/password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='includes/user/password_reset_complete.html'),name="password_reset_complete"),
    path('<str:username>/', views.profileView,name="profileView"),
    path('<str:username>/settings/',UserUpdateView.as_view(),name='settings'),
   

   
]
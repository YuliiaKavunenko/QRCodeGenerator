from django.urls import path
from .views import render_user_page, render_registration_page, render_authorization_page, logout_user

urlpatterns = [
    path("user/", render_user_page, name="user"),
    path("user/registration", render_registration_page, name="registration"),
    path("user/authorization", render_authorization_page, name="authorization"),
    path("user/logout", logout_user, name="logout"),
]

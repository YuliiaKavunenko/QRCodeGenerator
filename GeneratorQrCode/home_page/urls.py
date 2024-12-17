from django.urls import path
from .views import render_home_page


urlpatterns = [
    path("", render_home_page, name = "home")
]
from .views import *
from django.urls import path


urlpatterns = [
    path('subscription_page/', render_subscription_page, name = "subscription"),
]

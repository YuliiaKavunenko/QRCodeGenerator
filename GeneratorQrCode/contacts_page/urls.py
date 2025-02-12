from .views import *
from django.urls import path


urlpatterns = [
    path('contacts_page/', render_contacts_page, name = "contacts"),
]

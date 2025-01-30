from .views import *
from django.urls import path


urlpatterns = [
    path('my_qrcodes_page/', render_myqrcodespage, name="myqrcodes")
]
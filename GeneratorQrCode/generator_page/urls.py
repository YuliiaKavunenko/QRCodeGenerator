from .views import *
from django.urls import path


urlpatterns = [
    path('generator_page/', render_generatorpage, name="generate")
]
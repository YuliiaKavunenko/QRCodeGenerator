"""
URL configuration for GeneratorQrCode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from generator_page.views import render_generatorpage
from my_qrcodes_page.views import render_myqrcodespage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("generator_page/", render_generatorpage, name="generate"),
    path("my_qrcodes_page/", render_myqrcodespage, name="myqrcodes")
    
    # path('contacts/', admin.site.urls),
    # path('generator_qrcodes/', admin.site.urls),
    # path('', admin.site.urls),
    # path('my_qrcodes/', admin.site.urls),
    # path('subscription_settings/', admin.site.urls),

    # path('user/', admin.site.urls),
]

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
from django.urls import path, include
from home_page.views import render_home_page
from user_page.views import render_user_page, render_registration_page, render_authorization_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_home_page, name = "home"),
    path('user/', render_user_page, name = "user"),
    path('user/registration', render_registration_page, name = "registration"),
    path('user/authorization', render_authorization_page, name = "home"),
    
    # path('contacts/', admin.site.urls),
    # path('generator_qrcodes/', admin.site.urls),
    # path('', admin.site.urls),
    # path('my_qrcodes/', admin.site.urls),
    # path('subscription_settings/', admin.site.urls),

    # path('user/', admin.site.urls),
]

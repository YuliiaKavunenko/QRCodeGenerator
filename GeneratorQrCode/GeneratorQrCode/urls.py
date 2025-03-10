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
from . import settings
from django.conf.urls.static import static
from django.urls import path
from home_page.views import render_home_page
from user_page.views import render_user_page, render_registration_page, render_authorization_page, logout_user
from generator_page.views import render_generatorpage
from my_qrcodes_page.views import render_myqrcodespage
from contacts_page.views import render_contacts_page
from subscription_page.views import render_subscription_page
from subscription_page.views import render_payment_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_home_page, name = "home"),
    path('user/', render_user_page, name = "user"),
    path('user/registration', render_registration_page, name = "registration"),
    path('user/authorization', render_authorization_page, name = "authorization"),
    path('user/logout', logout_user, name = "logout"),
    path("generator_page/", render_generatorpage, name = "generate"),
    path("my_qrcodes_page/", render_myqrcodespage, name = "myqrcodes"),
    path('contacts_page/', render_contacts_page, name = "contacts"),
    path('subscription_page/', render_subscription_page, name = "subscription"),
    path('payment_page/', render_payment_page, name = "payment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""tais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import tais.views

urlpatterns = [
    path(settings.PREFIX_URL + 'user_profile/', tais.views.index,
         name='user_profile'),
    path(settings.PREFIX_URL + 'trending/', tais.views.trending,
         name='trending'),
    path(settings.PREFIX_URL + 'today/', tais.views.today,
         name='today'),
    path(settings.PREFIX_URL + 'last_month/', tais.views.lastMonth,
         name='last_month'),
    path(settings.PREFIX_URL + '', tais.views.index, name='home'),
    path(settings.PREFIX_URL + 'admin/', admin.site.urls),
    path(settings.PREFIX_URL + 'accounts/', include(
                                                'django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

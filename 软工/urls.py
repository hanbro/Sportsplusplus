"""软工 URL Configuration

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
from django.urls import path,include
from rest_framework import routers
from app_user.user import views as user_view



urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/',user_view.login),
    path('register/',user_view.register),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('back_login/',user_view.back_user),
]

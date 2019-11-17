"""Clima URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from .Apps.GestionClima import views

urlpatterns = [
    path('', views.home, name="home"),
    path('statistics/', views.statistics, name="statistics"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact"),
    path('navbar/', views.navbar, name="navbar"),
    path('admin/', admin.site.urls),
]

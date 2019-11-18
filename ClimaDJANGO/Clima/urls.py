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
from django.urls import path, include

from .Apps.GestionClima import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('statistics/', views.statistics, name="statistics"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact"),
    path('navbar/', views.navbar, name="navbar"),
    path('add', views.add),
    path('edit/<int:tipoUser_id>', views.edit),
    path('edit/<int:instancia.id>', views.edit),
    path('delete/<int:tipoUser_id>', views.delete),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    #url para recuperacion de mail directorio users
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

        path('password-reset/',
             auth_views.PasswordResetView.as_view(
                 template_name='registration/password_reset_form.html'
             ),
             name='password_reset'),

        path('password-reset/done/',
             auth_views.PasswordResetDoneView.as_view(
                 template_name='registration/password_reset_done.html'
             ),
            name='password_reset_done'),

        path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
                 template_name='registration/password_reset_confirm.html'
             ),

             name='password_reset_confirm'),
        path('password-reset-complete/',
             auth_views.PasswordResetCompleteView.as_view(
                 template_name='registration/password_reset_complete.html'
             ),
            name='password_reset_complete'),
]

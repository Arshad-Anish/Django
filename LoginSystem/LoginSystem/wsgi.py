"""
WSGI config for LoginSystem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LoginSystem.settings")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("login/", include("home.urls")),
]

application = get_wsgi_application()

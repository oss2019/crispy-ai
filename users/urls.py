from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView #Required to link Templates

urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
]

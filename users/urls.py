from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView #Required to link Templates

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # home page for users
    path('', TemplateView.as_view(template_name='users/home.html'), name='Home')
]

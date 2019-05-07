"""
Created this Urls.py to route everything that is not related to
user authentication from this BaseApp.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="BaseApp"),
]

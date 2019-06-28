from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('register_course/', views.register_course, name='register_course'),
    path('create_lecture/', views.create_lecture, name='create_lecture')
]

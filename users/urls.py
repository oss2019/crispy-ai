from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # home page for users
    path('', views.home, name='Home'),
    # #login path only created to redirect after registrations
    # path('login',views.login,name='login'),
    #   Register Page
    path('register', views.register_user, name='register'),
    path('profile', views.user_profile, name='profile'),
    path('edit', views.profile_update, name='edit'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

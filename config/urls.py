# config/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import homepage, dashboard

urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
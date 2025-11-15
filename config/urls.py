# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Includi tutte le rotte definite nell'app 'core'
    path('', include('core.urls')), 
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
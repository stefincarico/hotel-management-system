# config/urls.py
from django.contrib import admin
from django.urls import path, include  # <-- Assicurati di importare 'include'

from core.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    
    # Aggiungi questa riga. Delega la gestione di tutti gli URL
    # che iniziano con 'accounts/' al sistema di autenticazione di Django.
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('admin/', admin.site.urls),
]
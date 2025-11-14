# config/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import homepage, dashboard, select_hotel, activate_hotel

urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'), 
    path('select-hotel/', select_hotel, name='select_hotel'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # Questo URL cattura un numero intero (l'ID dell'hotel) e lo passa
    # alla view 'activate_hotel' come argomento 'hotel_id'.
    path('activate-hotel/<int:hotel_id>/', activate_hotel, name='activate_hotel'), 
]
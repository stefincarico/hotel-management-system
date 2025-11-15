# config/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import get_add_room_button, homepage, dashboard, select_hotel, activate_hotel,update_room_form,update_room, room_list, toggle_room_status, create_room_form, create_room




urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'), 
    path('select-hotel/', select_hotel, name='select_hotel'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # Questo URL cattura un numero intero (l'ID dell'hotel) e lo passa
    # alla view 'activate_hotel' come argomento 'hotel_id'.
    path('activate-hotel/<int:hotel_id>/', activate_hotel, name='activate_hotel'), 
    path('rooms/', room_list, name='room_list'),
    path('rooms/toggle-status/<int:room_id>/', toggle_room_status, name='toggle_room_status'),
    path('rooms/create-form/', create_room_form, name='create_room_form'),
    path('rooms/create/', create_room, name='create_room'),
    path('rooms/add-button/', get_add_room_button, name='get_add_room_button'),
    path('rooms/update-form/<int:room_id>/', update_room_form, name='update_room_form'), 
    path('rooms/update/<int:room_id>/', update_room, name='update_room'),
]


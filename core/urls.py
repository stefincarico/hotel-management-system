# core/urls.py
from django.urls import path
from .views import (
    homepage, dashboard, select_hotel, activate_hotel, room_list,
    toggle_room_status, create_room_form, create_room, update_room_form,
    update_room, get_add_room_button, get_room_card
)

app_name = 'core'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('select-hotel/', select_hotel, name='select_hotel'),
    path('activate-hotel/<int:hotel_id>/', activate_hotel, name='activate_hotel'),
    
    # Rotte per le Camere
    path('rooms/', room_list, name='room_list'),
    path('rooms/toggle-status/<int:room_id>/', toggle_room_status, name='toggle_room_status'),
    path('rooms/create-form/', create_room_form, name='create_room_form'),
    path('rooms/create/', create_room, name='create_room'),
    path('rooms/update-form/<int:room_id>/', update_room_form, name='update_room_form'),
    path('rooms/update/<int:room_id>/', update_room, name='update_room'),
    path('rooms/add-button/', get_add_room_button, name='get_add_room_button'),
    path('rooms/card/<int:room_id>/', get_room_card, name='get_room_card'),
]
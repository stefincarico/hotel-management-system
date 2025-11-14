# core/admin.py
from django.contrib import admin
from .models import User, Hotel, UserHotelRole

# Registriamo i modelli per renderli visibili nell'interfaccia di admin.
admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(UserHotelRole)
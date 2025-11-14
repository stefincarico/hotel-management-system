# core/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Hotel, UserHotelRole

# -----------------------------------------------------------------------------
# Configurazione per il modello USER
# -----------------------------------------------------------------------------
# Ereditiamo dalla UserAdmin di base di Django, che ha già tutta la logica 
# di sicurezza per le password e una visualizzazione dei campi sensata.
class CustomUserAdmin(BaseUserAdmin):
    # Qui potremmo aggiungere personalizzazioni, se in futuro aggiungeremo
    # campi al nostro modello User (es. 'phone_number'). Per ora va bene così.
    pass

# -----------------------------------------------------------------------------
# Configurazione per il modello HOTEL
# -----------------------------------------------------------------------------
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'created_at')
    list_filter = ('city',)
    search_fields = ('name',)

# -----------------------------------------------------------------------------
# Registrazione finale dei modelli
# -----------------------------------------------------------------------------
# Registriamo il nostro modello User usando la classe Admin personalizzata e sicura.
admin.site.register(User, CustomUserAdmin) 

# Il modello Hotel è già registrato grazie al decoratore @admin.register.

# Registriamo UserHotelRole in modo semplice, perché non ha logica complessa.
admin.site.register(UserHotelRole)
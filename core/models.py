# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.city})"
    
    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

class User(AbstractUser):
    # Per ora non aggiungiamo campi extra, ma la struttura è pronta.
    # Potremmo aggiungere in futuro:
    # phone_number = models.CharField(max_length=20, blank=True, null=True)
    pass # 'pass' significa che per ora non aggiungiamo nulla di nuovo

    def __str__(self):
        return self.get_full_name() or self.username
    
class UserHotelRole(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        MANAGER = 'MANAGER', 'Manager'
        RECEPTIONIST = 'RECEPTIONIST', 'Receptionist'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='roles')
    role = models.CharField(max_length=20, choices=Role.choices)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user', 'hotel']
        verbose_name = "User-Hotel Role"
        verbose_name_plural = "User-Hotel Roles"

    def __str__(self):
        return f"{self.user.username} @ {self.hotel.name} as {self.get_role_display()}"
    
class Room(models.Model):
    class RoomType(models.TextChoices):
        SINGLE = 'SINGLE', 'Singola'
        DOUBLE = 'DOUBLE', 'Doppia'
        SUITE = 'SUITE', 'Suite'
    
    class RoomStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Disponibile'
        MAINTENANCE = 'MAINTENANCE', 'In Manutenzione'
        OUT_OF_SERVICE = 'OUT_OF_SERVICE', 'Fuori Servizio'

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20, choices=RoomType.choices)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)

    status = models.CharField(
        max_length=20, 
        choices=RoomStatus.choices, 
        default=RoomStatus.AVAILABLE
    )

    class Meta:
        # Un numero di camera deve essere unico all'interno di un singolo hotel.
        # La stessa camera "101" può esistere in hotel diversi.
        unique_together = ['hotel', 'room_number']
        ordering = ['room_number']

    def __str__(self):
        return f"Camera {self.room_number} ({self.get_room_type_display()}) - {self.hotel.name}"
    

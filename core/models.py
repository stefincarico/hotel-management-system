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
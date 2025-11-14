# config/urls.py
from django.contrib import admin
from django.urls import path
from core.views import homepage  # <-- 1. IMPORTA LA TUA VIEW

urlpatterns = [
    # 2. COLLEGA L'URL ALLA VIEW
    path('', homepage, name='homepage'), # '' significa la root del sito (es. http://127.0.0.1:8000/)
    path('admin/', admin.site.urls),
]
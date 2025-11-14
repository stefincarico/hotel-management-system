# core/views.py
from django.shortcuts import render # <-- Cambia l'import

def homepage(request):
    # La funzione render fa tutto il lavoro pesante:
    # 1. Prende la request
    # 2. Prende il nome del file template ('homepage.html')
    # 3. Lo "renderizza" (cioè lo trasforma in HTML completo)
    # 4. Lo impacchetta in una HttpResponse e lo restituisce
    return render(request, 'homepage.html')
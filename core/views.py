# core/views.py
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# ... la tua view homepage ...
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required
def select_hotel(request):
    # Recuperiamo tutti i ruoli (e quindi gli hotel) associati all'utente corrente.
    # Grazie al related_name='roles' che abbiamo messo nel modello UserHotelRole,
    # possiamo fare questa query "inversa" in modo super elegante.
    user_roles = request.user.roles.filter(is_active=True)
    
    # Se un utente non ha ruoli attivi, non dovrebbe poter fare nulla.
    # Per ora, gli mostriamo una pagina con un avviso.
    if not user_roles.exists():
        # Qui potremmo renderizzare un template "access_denied.html"
        return HttpResponse("Non hai accesso a nessun hotel. Contatta l'amministratore.", status=403)

    # Estraiamo la lista di hotel unici dai ruoli
    hotels = [role.hotel for role in user_roles]
    
    context = {
        'hotels': hotels
    }
    return render(request, 'select_hotel.html', context)
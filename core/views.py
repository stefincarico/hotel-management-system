# core/views.py
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST 
from django.shortcuts import redirect
from django.template.loader import render_to_string
import json

from core.models import Hotel, Room


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

@login_required
def activate_hotel(request, hotel_id):
    # 1. CONTROLLO DI SICUREZZA FONDAMENTALE
    # Verifichiamo che l'utente abbia un ruolo attivo per l'hotel richiesto.
    # Se un utente prova a "indovinare" l'URL con un ID di un hotel a cui non 
    # ha accesso, questa query non restituirà nulla.
    can_access = request.user.roles.filter(hotel_id=hotel_id, is_active=True).exists()

    if not can_access:
        # Se non ha accesso, gli neghiamo il permesso.
        return HttpResponse("Accesso negato. Non hai un ruolo attivo in questo hotel.", status=403)

    # 2. SALVATAGGIO IN SESSIONE
    # La sessione di Django è come un dizionario Python. Possiamo scriverci dentro
    # quello che vogliamo. Il dato verrà salvato sul server e legato al cookie
    # del browser dell'utente.
    request.session['active_hotel_id'] = hotel_id
    
    # 3. REDIRECT AL DASHBOARD
    # Ora che l'hotel è "attivo", mandiamo l'utente al suo pannello di controllo.
    return redirect('dashboard')

@login_required
def dashboard(request):
    # Leggiamo l'ID dell'hotel attivo dalla sessione.
    # Usiamo .get() che è più sicuro: se la chiave non esiste, restituisce None invece di un errore.
    active_hotel_id = request.session.get('active_hotel_id')

    # Se non c'è un hotel attivo, forse l'utente è arrivato qui per sbaglio.
    # Lo rimandiamo alla pagina di selezione.
    if not active_hotel_id:
        return redirect('select_hotel')

    # Recuperiamo l'oggetto Hotel dal database per poter mostrare il suo nome.
    # get_object_or_404 è una scorciatoia che restituisce un oggetto o una pagina 404 Not Found
    # se l'oggetto con quell'ID non esiste. È ottimo per la robustezza.
    active_hotel = get_object_or_404(Hotel, pk=active_hotel_id)

    context = {
        'active_hotel': active_hotel
    }
    return render(request, 'dashboard.html', context)

@login_required
def room_list(request):
    # !! CONTROLLO DI SICUREZZA FONDAMENTALE !!
    # Prendiamo l'hotel attivo dalla sessione. Se non c'è, l'utente non è autorizzato.
    active_hotel_id = request.session.get('active_hotel_id')
    if not active_hotel_id:
        return HttpResponse("Seleziona prima un hotel.", status=403)
    
    # Filtriamo le camere SOLO per l'hotel attivo.
    rooms = Room.objects.filter(hotel_id=active_hotel_id)
    
    context = {
        'rooms': rooms,
        'active_hotel': Hotel.objects.get(pk=active_hotel_id) # Ci serve per il titolo
    }
    return render(request, 'room_list.html', context)

# core/views.py

@require_POST
@login_required
def toggle_room_status(request, room_id):
    active_hotel_id = request.session.get('active_hotel_id')
    if not active_hotel_id:
        return HttpResponse("Azione non permessa.", status=403)

    # Il controllo di sicurezza è identico e sempre fondamentale
    room = get_object_or_404(Room, pk=room_id, hotel_id=active_hotel_id)
    
    # Logica di "toggle": se è DISPONIBILE la mettiamo FUORI SERVIZIO,
    # altrimenti la rimettiamo DISPONIBILE.
    if room.status == Room.RoomStatus.AVAILABLE:
        room.status = Room.RoomStatus.OUT_OF_SERVICE
    else:
        room.status = Room.RoomStatus.AVAILABLE
    
    room.save()
    
    # Ora la parte nuova: invece di una risposta vuota, renderizziamo
    # un "partial template", passandogli solo l'oggetto 'room' aggiornato.
    context = {'room': room}
    return render(request, 'partials/room_card.html', context)

@login_required
def create_room_form(request):
    # Questa view serve solo a restituire il pezzo di HTML del form.
    # Non ha logica complessa.
    return render(request, 'partials/room_form.html')

@login_required
def get_add_room_button(request):
    # Questa view serve solo a restituire il pezzo di HTML del pulsante
    return render(request, 'partials/add_room_button.html')

@require_POST
@login_required
def create_room(request):
    active_hotel_id = request.session.get('active_hotel_id')
    if not active_hotel_id:
        return HttpResponse("Azione non permessa.", status=403)

    new_room = Room.objects.create(
        hotel_id=active_hotel_id,
        room_number=request.POST.get('room_number'),
        room_type=request.POST.get('room_type'),
        price_per_night=request.POST.get('price_per_night'),
    )
    
    # Prepariamo il contesto per DUE frammenti
    context = {'room': new_room}

    # Rendiamo la card della nuova camera
    room_card_html = render_to_string('partials/room_card.html', context)
    
    # E rendiamo il pulsante "Aggiungi" per resettare il form
    add_button_html = render_to_string('partials/add_room_button.html', {})

    # Uniamo i due frammenti HTML. HTMX li processerà entrambi.
    html_response = room_card_html + add_button_html
    
    return HttpResponse(html_response)

@login_required
def update_room_form(request, room_id):
    active_hotel_id = request.session.get('active_hotel_id')
    if not active_hotel_id:
        return HttpResponse("Azione non permessa.", status=403)

    # Recuperiamo la stanza specifica da modificare, sempre con il controllo di sicurezza
    room = get_object_or_404(Room, pk=room_id, hotel_id=active_hotel_id)
    
    # Passiamo l'oggetto 'room' al template. Lo useremo per pre-compilare i campi.
    context = {'room': room}
    return render(request, 'partials/room_form.html', context)

@require_POST
@login_required
def update_room(request, room_id):
    active_hotel_id = request.session.get('active_hotel_id')
    if not active_hotel_id:
        return HttpResponse("Azione non permessa.", status=403)

    # Recuperiamo la stanza da aggiornare, sempre con la massima sicurezza
    room = get_object_or_404(Room, pk=room_id, hotel_id=active_hotel_id)
    
    # Aggiorniamo i campi dell'oggetto con i nuovi dati
    room.room_number = request.POST.get('room_number')
    room.room_type = request.POST.get('room_type')
    room.price_per_night = request.POST.get('price_per_night')
    room.save()
    
    # 1. Prepariamo il template della card aggiornata
    context = {'room': room}
    html = render_to_string('partials/room_card.html', context, request=request)
    
    # 2. Prepariamo il template della card aggiornata
    context = {'room': room}
    room_card_html = render_to_string('partials/room_card.html', context, request=request)
    
    # 3. Strategia JavaScript nativa per il Toast
    # Creiamo un payload JSON per il nostro evento
    trigger_payload = {
        "message": f"Camera {room.room_number} aggiornata con successo!",
        "level": "success"
    }
    payload_json = json.dumps(trigger_payload)

    # Creiamo un tag <script> che verrà eseguito da HTMX dopo lo swap.
    # Questo approccio è il più robusto perché usa le API native del browser
    # e non si affida all'inizializzazione di Alpine.js (x-init).
    toast_trigger_script = f"""
    <script>
        // Chiamiamo direttamente il metodo showToast esposto globalmente
        if (window.showToast) {{
            window.showToast({payload_json});
        }} else {{
            // Fallback o log per debug se window.showToast non è ancora disponibile
            console.error("window.showToast non è definito. Alpine.js potrebbe non essere caricato o inizializzato correttamente.");
        }}
    </script>
    """
    
    # 4. Uniamo l'HTML principale e lo script
    final_html = room_card_html + toast_trigger_script
    
    return HttpResponse(final_html)

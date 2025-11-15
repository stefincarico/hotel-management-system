# 📝 BLUEPRINT E DIARIO DI BORDO

Questo documento traccia i progressi, le decisioni architetturali e le lezioni imparate durante lo sviluppo del Sistema di Gestione Hotel.

---

# 💡 DEBITO TECNICO E MIGLIORAMENTI FUTURI

Questa sezione documenta le aree dell'applicazione dove abbiamo consapevolmente scelto una soluzione semplificata per motivi didattici, con l'intenzione di migliorarla in futuro.

-   **Gestione Avanzata dello Stato delle Camere:**
    -   **Problema:** Il modello `Room` supporta tre stati (`AVAILABLE`, `MAINTENANCE`, `OUT_OF_SERVICE`), ma l'interfaccia utente attuale implementa solo un semplice "toggle" tra `AVAILABLE` e `OUT_OF_SERVICE`. Lo stato `MAINTENANCE` è inutilizzato.
    -   **Causa:** L'implementazione del toggle è servita come esercizio didattico per il pattern di HTMX "swap di un frammento HTML".
    -   **Soluzione Proposta:** In un modulo futuro, sostituire il singolo pulsante "toggle" con un'interfaccia più ricca (es. un dropdown con Alpine.js) che permetta a un utente autorizzato di impostare esplicitamente ciascuno dei tre stati. Questo richiederà una view più flessibile (`set_room_status` invece di `toggle_room_status`) che possa accettare lo stato desiderato come parametro.
    -   **Stato:** Da implementare.

---

## FASE 3: FRONTEND (In Corso)

### Modulo 7: HTMX (In Corso)
- **Obiettivo:** Trasformare le interfacce da "full-reload" a "partial-update" usando richieste AJAX.
- **Implementazione Chiave:**
    - **Soft Delete:** Sostituita la logica di cancellazione fisica (`Hard Delete`) delle camere con una cancellazione logica (`Soft Delete`), modificando il modello `Room` per includere un campo `status`. Questa decisione, guidata dalla logica di business, garantisce l'integrità dello storico dei dati.
    - **Pattern "Click to Edit":** Implementata la modifica "inline" delle camere. Cliccando "Modifica", la card della camera (`room_card.html`) viene sostituita con un form precompilato (`room_form.html`). Dopo l'invio, il server restituisce la card aggiornata, che a sua volta rimpiazza il form, chiudendo la modalità di modifica.
    - **Pattern "Toggle State":** Creata la prima interazione HTMX per cambiare lo stato di una camera (es. da Disponibile a Fuori Servizio). La view Django restituisce un frammento HTML (`partial template`) che HTMX usa per sostituire (`hx-swap`) l'elemento obsoleto nella pagina.
- **Lezioni Imparate:**
    - Identificata una discrepanza tra la flessibilità del modello dati (3 stati per la camera) e la semplicità dell'interfaccia utente (toggle tra 2 stati). Documentato come debito tecnico da risolvere in futuro.
    - **Targeting dinamico in HTMX:** Durante l'implementazione del pattern "Click to Edit", è emerso un problema: il form di modifica, sostituendo la card originale, ne eliminava anche l'ID (`#room-{{ room.id }}`). La soluzione è stata usare `hx-target="this"` e `hx-swap="outerHTML"` sul form stesso, rendendolo capace di auto-sostituirsi con la risposta del server (la card aggiornata). Questo approccio rende il componente più autonomo e robusto.
    - **Affidabilità degli Eventi HTMX:** Nell'implementare le notifiche "toast", si è scoperto che un evento `HX-Trigger` viene scatenato sull'elemento che subisce lo swap. Se questo elemento viene sostituito, la propagazione dell'evento (`event bubbling`) verso `window` può fallire. La soluzione robusta è specificare esplicitamente un target globale nel payload dell'header, es: `{"showMessage": {"target": "body", ...}}`. Questo garantisce che l'ascoltatore globale (`@showMessage.window`) riceva sempre l'evento.

### Modulo 6: Alpine.js (Completato)
- **Obiettivo Raggiunto:** Aggiunta di interattività client-side leggera.
- **Implementazione Chiave:** Creato un menu dropdown per il profilo utente, gestendo lo stato "aperto/chiuso" direttamente nell'HTML con `x-data`, `x-show` e `@click`.

### Modulo 5: Tailwind CSS (Completato)
- **Obiettivo Raggiunto:** Setup di un sistema di styling "utility-first" tramite la Standalone CLI (v3 stabile).
- **Lezioni Imparate:** Risolto un bug critico legato all'uso di una versione alpha instabile dello strumento.

---

## FASE 2: SICUREZZA (Completata)

### Modulo 4: Autorizzazione Multi-Tenant (Completato)
- **Architettura:** Implementato un sistema di selezione del "contesto tenant" post-login.
- **Meccanismo:** L'ID dell'hotel attivo (`active_hotel_id`) viene salvato in modo sicuro nella **sessione** lato server.
- **Sicurezza:** Ogni view che attiva un contesto verifica che l'utente abbia effettivamente un ruolo associato a quell'hotel, prevenendo manipolazioni dell'URL.

### Modulo 3: Autenticazione (Completato)
- **Componenti:** Implementato il flusso di Login/Logout sfruttando le view integrate di `django.contrib.auth`.
- **Protezione View:** Introdotto il decoratore `@login_required` per proteggere le pagine private.
- **Lezioni Imparate:**
    - Risolto un bug critico di sicurezza nell'Admin di Django. La registrazione base di un Custom User Model (`admin.site.register(User)`) non gestiva correttamente l'hashing delle password. Il problema è stato risolto creando una classe `CustomUserAdmin` che eredita dalla `BaseUserAdmin` di Django, garantendo la gestione sicura delle password.

---

## FASE 1: FONDAMENTA (Completata)

### Modulo 2: Database e Modelli (Completato)
- **Decisione Chiave:** Scelto **PostgreSQL** al posto di SQLite per allineare l'ambiente di sviluppo a quello di produzione.
- **Modelli:** Definiti i modelli `Hotel`, `User` (custom, da `AbstractUser`) e la tabella pivot `UserHotelRole` per la logica di accesso flessibile.
- **Gestione Segreti:** Implementato `python-decouple` per gestire le credenziali del database tramite un file `.env` ignorato da Git.

### Modulo 1: Django Fondamenti (Completato)
- Creato lo scheletro del progetto e la prima app (`core`).
- Implementato il ciclo MTV base con una view, un template e un URL.

### Modulo 0: Setup Ambiente (Completato)
- Configurato ambiente di sviluppo isolato con `venv`.
- Inizializzato repository Git e collegato a GitHub.
---
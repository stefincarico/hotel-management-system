# 📝 BLUEPRINT E DIARIO DI BORDO

Questo documento traccia i progressi, le decisioni architetturali e le lezioni imparate durante lo sviluppo del Sistema di Gestione Hotel.

---

## FASE 3: FRONTEND (In Corso)

### Modulo 5: Tailwind CSS (Completato)
- **Obiettivo:** Integrare un sistema di styling moderno e "utility-first".
- **Decisioni Chiave:**
    - Adottata la **Standalone CLI** di Tailwind per evitare di introdurre Node.js/NPM nel progetto Python, mantenendo il setup più snello.
- **Lezioni Imparate:**
    - **Criticità delle Versioni:** Affrontato e risolto un blocco critico causato dall'uso di una versione alpha instabile di Tailwind (`v4.x`). Il problema è stato risolto effettuando il downgrade alla più recente versione stabile (`v3.4.4`). Questo sottolinea l'importanza di utilizzare release stabili in sviluppo.
    - **Debugging Strumenti Esterni:** Imparato a isolare problemi non legati al codice Django ma agli strumenti della toolchain (l'eseguibile di Tailwind stesso).

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
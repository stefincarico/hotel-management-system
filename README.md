# 🏨 Sistema di Gestione Catena Hotel

Applicazione web multi-tenant per la gestione di hotel, costruita con Django, HTMX, Alpine.js e Tailwind CSS.

## Prerequisiti

Assicurati di avere installato sul tuo sistema:
- Python 3.11+
- Git
- PostgreSQL

## 🚀 Guida al Setup per lo Sviluppo

Segui questi passaggi per avviare il progetto in locale.

### 1. Clona il Repository
```bash
git clone <URL_DEL_TUO_REPOSITORY_GITHUB>
cd hotel-management-system
```

### 2. Crea e Attiva l'Ambiente Virtuale
```bash
# Crea l'ambiente
python -m venv venv

# Attiva l'ambiente (Windows)
.\venv\Scripts\activate
```

### 3. Installa le Dipendenze Python
Prima di tutto, creiamo il file delle dipendenze se non esiste:
```bash
pip freeze > requirements.txt
```
Ora, installa tutto:
```bash
pip install -r requirements.txt
```

### 4. Configura il Database PostgreSQL
1.  Apri `pgAdmin` o un altro client PostgreSQL.
2.  Crea un nuovo database vuoto. Il nome consigliato è `hotel_management_system_db`.

### 5. Configura le Variabili d'Ambiente
1.  Crea una copia del file di esempio: `copy .env.example .env` (su Windows).
2.  Apri il file `.env` e inserisci le credenziali corrette per il tuo database locale.

*(Nota: Dovrai creare un file `.env.example` con le chiavi ma senza i valori, da committare su Git)*

### 6. Applica le Migrazioni del Database
Questo comando creerà tutte le tabelle necessarie.
```bash
python manage.py migrate
```

### 7. Crea un Superuser
Questo utente ti servirà per accedere all'interfaccia di amministrazione di Django.
```bash
python manage.py createsuperuser
```

### 8. Avvia i Server di Sviluppo
Per lavorare al progetto, servono **due terminali aperti** nella cartella del progetto (con `venv` attivo).

**Terminale 1: Tailwind CSS Watcher**
Questo terminale scansiona i tuoi file HTML e rigenera il CSS automaticamente.
```bash
./bin/tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --watch
```

**Terminale 2: Django Development Server**
Questo è il server principale della tua applicazione.
```bash
python manage.py runserver
```

### 9. Accedi all'Applicazione
- **Sito Principale:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Django:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---
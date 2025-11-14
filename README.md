<h1 align="center">🏨 Hotel Manager</h1>
<h3 align="center">Un sistema di gestione alberghiera multi-tenant, multi-utente e basato sui ruoli — <em>senza JavaScript framework pesanti!</em></h3>

<p align="center">
  <a href="https://github.com/your-username/hotel-manager/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT" /></a>
  <a href="https://github.com/your-username/hotel-manager/actions/workflows/ci.yml"><img src="https://github.com/your-username/hotel-manager/actions/workflows/ci.yml/badge.svg" alt="CI Status" /></a>
  <a href="https://www.djangoproject.com"><img src="https://img.shields.io/badge/Framework-Django-092E20?logo=django" alt="Django" /></a>
  <a href="https://www.postgresql.org"><img src="https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql" alt="PostgreSQL" /></a>
  <a href="https://htmx.org"><img src="https://img.shields.io/badge/HTMX-1.9+-018FFC?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyLjUsMjAuNWwtNy41LTcuNUgxMlY2aDguNVYxM2g3LjVsLTcuNSw3LjV6Ii8+PC9zdmc+" alt="HTMX" /></a>
</p>

---

## 🌟 Visione del Progetto

**Hotel Manager** è un’applicazione didattica **leggera, performante e moderna**, costruita per dimostrare che puoi creare interfacce ricche **senza React, Vue o Angular**!  

Sfruttando la potenza di **Django**, **HTMX** e **Alpine.js**, questo sistema offre:
- 🏢 **Multi-tenancy**: ogni hotel è un tenant isolato (schema-based o domain-based)
- 👥 **Multi-utente**: ruoli distinti con permessi granulari
- 🔒 **RBAC (Role-Based Access Control)**: solo chi deve vedere/modificare, lo può fare
- 📱 **Interfaccia reattiva**: grazie a HTMX + Alpine.js, senza un singolo bundle JS pesante
- 🐳 **Pronto per la produzione**: Dockerizzato, con PostgreSQL e configurazione CI/CD
- ♿ **Accessibile**: rispetta i principi WCAG AA (grazie al markup semantico e ARIA)

> ✨ *Questo progetto è un omaggio allo sviluppo web semplice, veloce e umano.*  
> **Meno bundle. Più HTML. Tanta logica lato server. Zero ansia da npm.**

---

## 🛠️ Stack Tecnologico

| Livello             | Tecnologia                                                                 |
|---------------------|----------------------------------------------------------------------------|
| **Backend**         | Django 5 + Django REST Framework (solo dove serve)                         |
| **Database**        | PostgreSQL (con supporto a schema separation per multi-tenancy)            |
| **Frontend Dinamico**| HTMX + Alpine.js (per logica UI leggera)                                 |
| **Stile**           | Tailwind CSS (via CDN o build light) + classi semantiche                   |
| **Infrastruttura**  | Docker + Docker Compose                                                    |
| **CI/CD**           | GitHub Actions (test, build immagine, deploy demo)                        |
| **Autenticazione**  | Django Auth + custom middleware per tenant isolation                      |

---

## 🎯 Funzionalità Principali

| Ruolo             | Cosa può fare                                                             |
|-------------------|---------------------------------------------------------------------------|
| **Admin Globale** | Crea nuovi hotel (tenant), gestisce utenti globali                         |
| **Manager**       | Configura camere, tariffe, visualizza report, gestisce lo staff           |
| **Receptionist**  | Effettua check-in/out, gestisce prenotazioni in tempo reale               |
| **Staff Pulizie** | Vede lista camere da pulire, aggiorna stato con un clic                   |

Tutto avviene con:
- ⚡ **Risposte istantanee** grazie a HTMX (swap parziale del DOM)
- 🧘 **Zero reload della pagina** (ma sempre SEO-friendly!)
- 🗃️ **Isolamento dei dati per tenant** (nessun hotel vede i dati di un altro)

---

## 🚀 Avviare il Progetto Localmente

Assicurati di avere **Docker** e **Docker Compose** installati.

1. **Clona il repository**
   ```bash
   git clone https://github.com/your-username/hotel-manager.git
   cd hotel-manager
   ```

2. **Avvia i container**
   ```bash
   docker-compose up --build
   ```

3. **Esegui le migrazioni (la prima volta)**
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Apri il browser**
   ```
   http://localhost:8000
   ```

> 💡 **Vuoi sviluppare senza Docker?** Crea un virtualenv, installa le dipendenze da `requirements.txt`, configura PostgreSQL locale e avvia con `python manage.py runserver`.

---

## 📦 Struttura del Progetto

```
hotel-manager/
├── docker-compose.yml         # Servizi: web, db, (opz. nginx)
├── Dockerfile                 # Immagine Django ottimizzata
├── backend/
│   ├── config/                # Settings multi-env
│   ├── tenants/               # Logica multi-tenant (middleware + models)
│   ├── users/                 # RBAC, gruppi, permessi
│   ├── bookings/              # Prenotazioni, check-in/out
│   └── rooms/                 # Camere, categorie, disponibilità
├── templates/                 # HTML semantico + HTMX swaps
├── static/                    # CSS (Tailwind), Alpine.js, icone
└── docs/                      # Architettura, sync, accessibilità
```

---

## 📚 Documentazione Interna

- 🗂️ `docs/ARCHITECTURE.md` → Multi-tenancy con Django (schema vs subdomain)
- 🔐 `docs/RBAC.md` → Come sono implementati ruoli e permessi
- 🔄 `docs/HTMX_PATTERNS.md` → Esempi di interazioni senza JS pesante
- ♿ `docs/ACCESSIBILITY.md` → WCAG compliance con HTMX + ARIA

---

## 🤝 Contribuire

Questo è un **progetto didattico aperto a tutti**, specialmente a chi ama il backend pulito e il frontend leggero.

Sei:
- 🐍 un fan di Django?
- 💡 curioso di HTMX?
- 🐳 appassionato di Docker?

**Contribuisci!**  
Apri una issue, proponi una PR, o semplicemente chiedi chiarimenti.  
Ogni domanda rende la community più forte. ❤️

---

## 📄 Licenza

Distribuito sotto licenza **MIT**.  
Vedi [`LICENSE`](LICENSE) per i dettagli.

---

<p align="center">
  <em>Costruito con ❤️, HTML semantico e tanta tazza di tè ☕</em><br>
  <sub>Per chi crede che il web possa essere semplice, veloce e umano.</sub>
</p>

---

> ✨ **Pro tip**: premi `h` in qualsiasi pagina per aprire la guida rapida dei tasti di scelta rapida!


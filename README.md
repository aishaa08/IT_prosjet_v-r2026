# hei
# Intranett Server Project

## Beskrivelse

Dette prosjektet er et intranett-system for en liten bedrift. Systemet kjører på en Raspberry Pi-server med Ubuntu/Linux og skal gi ansatte tilgang til en intern nettside med nyttig informasjon om serveren og tjenester i bedriften.

Prosjektet bruker Python og MariaDB for å samle og lagre systeminformasjon fra serveren, som CPU-bruk og RAM-bruk. Denne informasjonen kan senere vises i et web-dashboard laget med Flask.

Formålet med prosjektet er å vise ferdigheter innen:

* Linux serveradministrasjon
* Python scripting
* databasehåndtering (MariaDB)
* Git og versjonskontroll
* nettverk og serverdrift

Prosjektet er laget som en del av et IT-drift / IT-konsulent skoleprosjekt.

---

## Teknologier brukt

* Python
* MariaDB
* Flask (webapplikasjon)
* Git / GitHub
* Linux / Ubuntu
* Raspberry Pi server

---

## Prosjektstruktur

IT_prosject2026_vår
│
├── README.md
├── main.py

├── scripts
│   └── monitor.py

├── uploads

└── logs

---

## Funksjoner (planlagt)

* Samle CPU og RAM informasjon fra server
* Lagre systemdata i MariaDB
* Lage en intern nettside med Flask
* Vise serverstatus i et dashboard
* Filopplasting for ansatte
* Loggføring av serverhendelser

---

## TODO Liste eksempel på VS

### Grunnsystem

* [ ] Lage prosjektstruktur
* [ ] Lage server monitor script
* [ ] Installere nødvendige Python pakker
* [ ] Teste monitor script på Raspberry Pi

### Database

* [ ] Opprette MariaDB database
* [ ] Lage tabell for systemstatus
* [ ] Lagre CPU og RAM data i databasen

### Automatisering

* [ ] Kjøre monitor script automatisk med cron
* [ ] Lage logging system

### Webapplikasjon

* [ ] Lage Flask server
* [ ] Lage login side
* [ ] Lage dashboard side
* [ ] Vise serverstatus på nettsiden

### Ekstra funksjoner

* [ ] Filopplasting
* [ ] Brukerhåndtering
* [ ] Bedre design på nettsiden

---

## Mål

Målet med prosjektet er å lage et fungerende intranett-system som viser serverstatus og demonstrerer praktiske ferdigheter innen IT-drift og systemadministrasjon.

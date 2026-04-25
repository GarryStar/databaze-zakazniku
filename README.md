🧾 Customer & Payment System (FastAPI)

Jednoduchý backend projekt pro správu zákazníků, jejich služeb a kontrolu plateb (např. podle variabilního symbolu).

🚀 Funkce
správa zákazníků
definice služeb (např. doména, internet)
přiřazení služby zákazníkovi
generování variabilního symbolu
příprava na párování plateb z banky
🧱 Technologie
Python
FastAPI
SQLAlchemy
SQLite
Uvicorn
📁 Struktura projektu
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── routers/
    ├── customers.py
    ├── services.py
    └── customer_services.py
⚙️ Instalace
python -m venv .venv
source .venv/bin/activate   # Linux
# nebo
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
▶️ Spuštění
uvicorn app.main:app --reload

API poběží na:

http://127.0.0.1:8000

Dokumentace:

http://127.0.0.1:8000/docs
🗄️ Databáze

Používá se SQLite (soubor customers.db).

Tabulky:

customers – zákazníci
services – typy služeb
customer_services – přiřazené služby zákazníkům
payments – přijaté platby
🔢 Variabilní symbol

Každá služba zákazníka má unikátní variabilní symbol:

[service_code][customer_service_id]

Příklad:

1000000001
10 = typ služby
00000001 = ID záznamu
📡 API endpointy
Zákazníci
GET     /customers
POST    /customers
GET     /customers/{id}
DELETE  /customers/{id}
Služby
GET     /services
POST    /services
Služby zákazníků
GET     /customer-services
POST    /customer-services
Zákazník + služby
GET /customers/{id}/services
🧠 Budoucí rozšíření
párování plateb z banky (API)
kontrola zaplaceno / nezaplaceno
frontend (HTML / JS)
autentizace (login)
Docker nasazení
⚠️ Poznámky
projekt je určen primárně pro lokální použití / učení
neřeší bezpečnost (zatím)
databáze se při změně modelu smaže a vytvoří znovu
👨‍💻 Autor

David 😄
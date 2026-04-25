# 🧾 Customer & Payment System (FastAPI)

Jednoduchý backend projekt pro správu zákazníků, jejich služeb a kontrolu plateb.

---

## 🚀 Funkce

* správa zákazníků
* definice služeb (např. doména, internet)
* přiřazení služby zákazníkovi
* generování variabilního symbolu
* příprava na párování plateb

---

## 🧱 Technologie

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

## 📁 Struktura projektu

```
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── routers/
    ├── customers.py
    ├── services.py
    └── customer_services.py
```

---

## ⚙️ Instalace

```bash
python -m venv .venv

# Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Spuštění

```bash
uvicorn app.main:app --reload
```

API poběží na:

```
http://127.0.0.1:8000
```

Dokumentace:

```
http://127.0.0.1:8000/docs
```

---

## 🗄️ Databáze

Používá se SQLite (soubor `customers.db`).

Tabulky:

* `customers`
* `services`
* `customer_services`
* `payments`

---

## 🔢 Variabilní symbol

Každá služba zákazníka má unikátní variabilní symbol:

```
[service_code][customer_service_id]
```

Příklad:

```
1000000001
```

---

## 📡 API endpointy

### Zákazníci

```
GET     /customers
POST    /customers
GET     /customers/{id}
DELETE  /customers/{id}
```

### Služby

```
GET     /services
POST    /services
```

### Služby zákazníků

```
GET     /customer-services
POST    /customer-services
```

### Zákazník + služby

```
GET /customers/{id}/services
```

---

## 🧠 Budoucí rozšíření

* párování plateb z banky
* kontrola zaplaceno / nezaplaceno
* jednoduchý frontend
* autentizace
* Docker

---

## ⚠️ Poznámky

* projekt je určen primárně pro lokální použití
* databáze se při změně modelu maže

---

## 👨‍💻 Autor

Gary 😄

import random
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.database import SessionLocal, Base, engine
from app.models import Customer


DATA_DIR = Path("data")

FIRST_NAMES_FILE = DATA_DIR / "m_jmena.csv"
LAST_NAMES_FILE = DATA_DIR / "m_prijmeni.txt"
STREETS_FILE = DATA_DIR / "ulice.txt"
POSTAL_CITIES_FILE = DATA_DIR / "psc_obce.txt"

EMAIL_DOMAINS = [
    "seznam.cz",
    "email.cz",
    "gmail.com",
    "centrum.cz",
    "post.cz",
]


def load_simple_file(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def load_first_names(path: Path) -> list[str]:
    names = []

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            # kdyby CSV mělo víc sloupců, vezme první
            name = line.split(";")[0].split(",")[0].strip()
            names.append(name)

    return names


def load_postal_cities(path: Path) -> list[tuple[str, str]]:
    result = []

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            postal_code, city = line.split(";", 1)
            result.append((postal_code.strip(), city.strip()))

    return result


def normalize_email_part(text: str) -> str:
    replacements = {
        "á": "a", "č": "c", "ď": "d", "é": "e", "ě": "e",
        "í": "i", "ň": "n", "ó": "o", "ř": "r", "š": "s",
        "ť": "t", "ú": "u", "ů": "u", "ý": "y", "ž": "z",
    }

    text = text.lower()

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"[^a-z0-9]", "", text)

    return text


def generate_phone() -> str:
    return f"+420 {random.randint(600, 799)} {random.randint(100, 999)} {random.randint(100, 999)}"


def generate_email(first_name: str, last_name: str) -> str:
    first = normalize_email_part(first_name)
    last = normalize_email_part(last_name)
    number = random.randint(1, 9999)
    domain = random.choice(EMAIL_DOMAINS)

    variants = [
        f"{first}.{last}{number}@{domain}",
        f"{last}.{first}{number}@{domain}",
        f"{first}{last}{number}@{domain}",
    ]

    return random.choice(variants)


def generate_bank_account() -> str:
    prefix = random.choice(["", f"{random.randint(10, 999999)}-"])
    account = random.randint(100000000, 9999999999)
    bank_code = random.choice(["0100", "0300", "0600", "0800", "2010", "3030", "5500"])

    return f"{prefix}{account}/{bank_code}"


def create_random_customer(
    first_names: list[str],
    last_names: list[str],
    streets: list[str],
    postal_cities: list[tuple[str, str]],
) -> Customer:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    street = random.choice(streets)
    postal_code, city = random.choice(postal_cities)

    return Customer(
        first_name=first_name,
        last_name=last_name,
        street=street,
        house_number=str(random.randint(1, 999)),
        city=city,
        postal_code=postal_code,
        email=generate_email(first_name, last_name),
        phone=generate_phone(),
        bank_account=generate_bank_account(),
    )


def main(count: int = 500):
    Base.metadata.create_all(bind=engine)

    first_names = load_first_names(FIRST_NAMES_FILE)
    last_names = load_simple_file(LAST_NAMES_FILE)
    streets = load_simple_file(STREETS_FILE)
    postal_cities = load_postal_cities(POSTAL_CITIES_FILE)

    db = SessionLocal()

    try:
        customers = [
            create_random_customer(
                first_names=first_names,
                last_names=last_names,
                streets=streets,
                postal_cities=postal_cities,
            )
            for _ in range(count)
        ]

        db.add_all(customers)
        db.commit()

        print(f"Hotovo. Vloženo zákazníků: {count}")

    finally:
        db.close()


if __name__ == "__main__":
    main(500)
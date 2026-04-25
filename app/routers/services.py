from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Service
from app.schemas import ServiceCreate, ServiceRead

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.post("/", response_model=ServiceRead)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    existing = db.query(Service).filter(Service.code == service.code).first()

    if existing:
        raise HTTPException(status_code=400, detail="Služba s tímto kódem už existuje")

    db_service = Service(**service.model_dump())

    db.add(db_service)
    db.commit()
    db.refresh(db_service)

    return db_service


@router.get("/", response_model=list[ServiceRead])
def get_services(db: Session = Depends(get_db)):
    return db.query(Service).all()
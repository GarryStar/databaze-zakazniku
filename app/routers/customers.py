from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Customer, CustomerService
from app.schemas import CustomerCreate, CustomerRead
from sqlalchemy.orm import joinedload
from app.schemas import CustomerWithServicesRead

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/", response_model=CustomerRead)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(**customer.model_dump())

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


@router.get("/", response_model=list[CustomerRead])
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()


@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if customer is None:
        raise HTTPException(status_code=404, detail="Zákazník nenalezen")

    return customer


@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if customer is None:
        raise HTTPException(status_code=404, detail="Zákazník nenalezen")

    db.delete(customer)
    db.commit()

    return {"message": "Zákazník smazán"}

@router.get("/{customer_id}/services", response_model=CustomerWithServicesRead)
def get_customer_with_services(customer_id: int, db: Session = Depends(get_db)):
    customer = (
        db.query(Customer)
        .options(
            joinedload(Customer.services).joinedload(CustomerService.service)
        )
        .filter(Customer.id == customer_id)
        .first()
    )

    if customer is None:
        raise HTTPException(status_code=404, detail="Zákazník nenalezen")

    return customer
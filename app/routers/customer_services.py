from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Customer, Service, CustomerService
from app.schemas import CustomerServiceCreate, CustomerServiceRead

router = APIRouter(
    prefix="/customer-services",
    tags=["Customer services"]
)


def generate_variable_symbol(service_code: str, customer_service_id: int) -> str:
    return f"{service_code}{customer_service_id:08d}"


@router.post("/", response_model=CustomerServiceRead)
def assign_service_to_customer(
    data: CustomerServiceCreate,
    db: Session = Depends(get_db),
):
    customer = db.query(Customer).filter(Customer.id == data.customer_id).first()

    if customer is None:
        raise HTTPException(status_code=404, detail="Zákazník nenalezen")

    service = db.query(Service).filter(Service.id == data.service_id).first()

    if service is None:
        raise HTTPException(status_code=404, detail="Služba nenalezena")

    customer_service = CustomerService(
        customer_id=data.customer_id,
        service_id=data.service_id,
        price=service.default_price,
        start_date=data.start_date,
        note=data.note,
    )

    db.add(customer_service)
    db.commit()
    db.refresh(customer_service)

    customer_service.variable_symbol = generate_variable_symbol(
        service_code=service.code,
        customer_service_id=customer_service.id,
    )

    db.commit()
    db.refresh(customer_service)

    return customer_service


@router.get("/", response_model=list[CustomerServiceRead])
def get_customer_services(db: Session = Depends(get_db)):
    return db.query(CustomerService).all()
from datetime import date
from pydantic import BaseModel

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    street: str | None = None
    house_number: str | None = None
    city: str | None = None
    postal_code: str | None = None
    email: str | None = None
    phone: str | None = None
    active: bool = True


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class ServiceBase(BaseModel):
    code: str
    name: str
    description: str | None = None
    default_price: int = 0
    active: bool = True


class ServiceCreate(ServiceBase):
    pass


class ServiceRead(ServiceBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class CustomerServiceCreate(BaseModel):
    customer_id: int
    service_id: int
    start_date: date | None = None
    note: str | None = None


class CustomerServiceRead(BaseModel):
    id: int
    customer_id: int
    service_id: int
    variable_symbol: str | None
    price: int
    active: bool
    start_date: date | None
    end_date: date | None
    note: str | None

    model_config = {
        "from_attributes": True
    }

class CustomerServiceWithServiceRead(BaseModel):
    id: int
    variable_symbol: str | None
    price: int
    active: bool
    start_date: date | None
    end_date: date | None
    note: str | None
    service: ServiceRead

    model_config = {
        "from_attributes": True
    }


class CustomerWithServicesRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    street: str | None
    house_number: str | None
    city: str | None
    postal_code: str | None
    email: str | None
    phone: str | None
    active: bool
    services: list[CustomerServiceWithServiceRead]

    model_config = {
        "from_attributes": True
    }
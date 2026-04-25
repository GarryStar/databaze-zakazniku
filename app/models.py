from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    street = Column(String, nullable=True)
    house_number = Column(String, nullable=True)
    city = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)

    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)

    active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    services = relationship(
        "CustomerService",
        back_populates="customer",
        cascade="all, delete-orphan",
    )


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    default_price = Column(Integer, nullable=False, default=0)
    active = Column(Boolean, default=True, nullable=False)

    customer_services = relationship(
        "CustomerService",
        back_populates="service",
    )


class CustomerService(Base):
    __tablename__ = "customer_services"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)

    variable_symbol = Column(String, unique=True, index=True, nullable=True)

    price = Column(Integer, nullable=False, default=0)
    active = Column(Boolean, default=True, nullable=False)

    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    note = Column(Text, nullable=True)

    customer = relationship(
        "Customer",
        back_populates="services",
    )

    service = relationship(
        "Service",
        back_populates="customer_services",
    )

    payments = relationship(
        "Payment",
        back_populates="customer_service",
    )


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    customer_service_id = Column(
        Integer,
        ForeignKey("customer_services.id"),
        nullable=True,
    )

    amount = Column(Integer, nullable=False)
    paid_at = Column(Date, nullable=False)

    variable_symbol = Column(String, index=True, nullable=True)
    sender_account = Column(String, nullable=True)
    bank_transaction_id = Column(String, unique=True, nullable=True)

    message = Column(Text, nullable=True)
    raw_data = Column(Text, nullable=True)

    matched = Column(Boolean, default=False, nullable=False)

    customer_service = relationship(
        "CustomerService",
        back_populates="payments",
    )
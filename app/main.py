from fastapi import FastAPI

from app.database import Base, engine
from app.routers import customers
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.routers import customers, services, customer_services

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Databáze zákazníků",
    version="0.1.0"
)

app.include_router(customers.router)
app.include_router(services.router)
app.include_router(customer_services.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pro testování OK
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customers.router)


@app.get("/")
def root():
    return {"message": "API pro zákazníky běží"}
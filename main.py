import datetime

import zoneinfo

from fastapi import FastAPI

from db import SessionDep, create_db
from models import Customer, Transaction, Invoice, CustomerCreate
from sqlmodel import select

app = FastAPI(lifespan=create_db)


@app.get("/")
async def index():
    return {"message": "Hello World"}


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}")
async def time(iso_code: str):
    print(iso_code)
    code = country_timezones.get(iso_code.upper())
    tz = zoneinfo.ZoneInfo(code)
    return {"time": datetime.datetime.now(tz)}


current_id: int = 0
db_customers: list[Customer] = []


@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)

    return customer


@app.get("/customers", response_model=list[Customer])
async def list_customers(session: SessionDep):
    return session.exec(select(Customer)).all()


@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):
    return transaction_data


@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    return invoice_data

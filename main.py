import datetime
import uuid
import zoneinfo

from fastapi import FastAPI

from models import Customer, Transaction, Invoice

app = FastAPI()


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


@app.post("/customers")
async def create_customer(customer_data: Customer):
    return customer_data


@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):
    return transaction_data


@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    return invoice_data

from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    description: str | None
    email: str
    age: int


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: str | None = None


class Transaction(BaseModel):
    id: int
    amount: int
    description: str


class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def total(self):
        return sum(transaction.amount for transaction in self.transactions)

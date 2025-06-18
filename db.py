#from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session, create_engine, SQLModel

sql_engine = 'db.sqlite3'
sql_url = f'sqlite:///{sql_engine}'

engine = create_engine(sql_url)


# @asynccontextmanager
def create_db(app: FastAPI):
    SQLModel.metadata.create_all(bind=engine)
    yield

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

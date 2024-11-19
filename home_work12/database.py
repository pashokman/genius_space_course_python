import os

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

from dotenv import load_dotenv

load_dotenv()


class Hero(SQLModel, table=True):
    id: int = Field(index=True, primary_key=True)
    name: str = Field()
    age: int = Field()
    email: str | None = Field(default=None)
    description: str | None = Field(default=None)
    company: int = Field(default=1)


# postgresql_url = f"postgresql://user:password@postgresserver/db"
postgresql_url = os.getenv("POSTGRESQL_URL")

engine = create_engine(postgresql_url)

conn = engine.connect()
print(conn.get_isolation_level())
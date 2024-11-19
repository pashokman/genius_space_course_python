import os

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship

from dotenv import load_dotenv

load_dotenv()


class User(SQLModel, table=True):
    id: int = Field(index=True, primary_key=True)
    name: str = Field()
    age: int = Field()
    email: str | None = Field(default=None)
    description: str | None = Field(default=None)
    company: int = Field(default=1, foreign_key="company.id")

    company_details: "Company" = Relationship(back_populates="employees")


class Company(SQLModel, table=True):
    id: int = Field(index=True, primary_key=True)
    name: str = Field()
    count_of_emloyes : int = Field()

    employees: list["User"] = Relationship(back_populates="company_details")


# postgresql_url = f"postgresql://user:password@postgresserver/db"
postgresql_url = os.getenv("POSTGRESQL_URL")

engine = create_engine(postgresql_url)

conn = engine.connect()
print(conn.get_isolation_level())


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/companies/")
def create_company(company: Company, session: SessionDep) -> User:
    session.add(company)
    session.commit()
    session.refresh(company)
    return company


@app.post("/users/")
def create_users(user: User, session: SessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get("/users/")
def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@app.get("/users/{user_id}")
def read_user(user_id: int, session: SessionDep) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}

@app.get("/debug/users")
def debug_users(session: SessionDep):
    users = session.exec(select(User)).all()
    return users
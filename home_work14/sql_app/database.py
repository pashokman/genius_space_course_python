import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

# postgresql_url = f"postgresql://user:password@postgresserver/db"
postgresql_url = os.getenv("POSTGRESQL_URL")

engine = create_engine(postgresql_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

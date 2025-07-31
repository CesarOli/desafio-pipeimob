from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

POSTGRES_USER = os.getenv("POSTGRES_USER", "pipeimob_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "supersecretpassword")
POSTGRES_DB = os.getenv("POSTGRES_DB", "pipeimob_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print("POSTGRES_USER:", os.getenv("POSTGRES_USER"))
print("POSTGRES_PASSWORD:", os.getenv("POSTGRES_PASSWORD"))
print("POSTGRES_DB:", os.getenv("POSTGRES_DB"))
print("POSTGRES_HOST:", os.getenv("POSTGRES_HOST"))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
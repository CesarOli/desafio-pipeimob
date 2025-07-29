from fastapi import FastAPI
from app.core.db.database import engine, Base

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "API PipeImob rodando!"}
from fastapi import FastAPI
from app.api.v1.endpoints import book, webhook
from app.core.db.database import engine, Base

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "API PipeImob rodando!"}

app.include_router(book.router)
app.include_router(webhook.router)
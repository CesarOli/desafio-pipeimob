from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.endpoints import book, webhook
from app.core.db.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando a aplicação e criando as tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    yield
    print("Encerrando a aplicação.")

app = FastAPI(
    title="API de Livros - Desafio Pipeimob",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
def read_root():
    return {"msg": "API PipeImob rodando!"}

app.include_router(book.router, prefix="/api/v1")
app.include_router(webhook.router, prefix="/api/v1")
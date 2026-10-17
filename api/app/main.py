"""
Punto de entrada de la API (FastAPI).

Se ejecuta con:
    uvicorn app.main:app --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI

from .database import Base, engine
from .routers import categorias, productos

# Crear las tablas si todavía no existen.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tienda Virtual API",
    description="API REST que expone productos y categorías desde PostgreSQL.",
    version="1.0.0",
)

# Registrar las rutas de productos y categorías.
app.include_router(productos.router)
app.include_router(categorias.router)


@app.get("/")
def raiz():
    """Endpoint para comprobar que la API está funcionando."""
    return {"mensaje": "API de la Tienda Virtual funciona "} 
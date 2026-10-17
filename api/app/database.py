"""
Configuración de la conexión a PostgreSQL con SQLAlchemy "puro"
(sin Flask-SQLAlchemy, porque este servicio ya no es una app Flask).
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# TODO 1: Leer la URL de conexión desde las variables de entorno.
DATABASE_URL = os.environ["DATABASE_URL"]

# TODO 2: Crear el motor de conexión a PostgreSQL.
engine = create_engine(DATABASE_URL)

# TODO 3: Crear la fábrica de sesiones de base de datos.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Clase base para los modelos de la base de datos.
Base = declarative_base()


def get_db():
    """
    Entrega una sesión de base de datos a FastAPI.
    La sesión se cierra automáticamente al finalizar la petición.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
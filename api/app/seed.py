"""
Script de carga inicial (seed) de la base de datos.

A diferencia del Taller 2 (que usaba comandos "flask seed-db"), aquí es un
script independiente porque este servicio no usa el CLI de Flask.

Se ejecuta DENTRO del contenedor de la API:

    docker compose exec api python -m app.seed
"""

import json
import os

from .database import Base, SessionLocal, engine
from .models import Categoria, Producto

RUTA_PRODUCTOS = os.path.join(os.path.dirname(__file__), "..", "data", "productos.json")


def cargar_datos():
    # Se asegura de que las tablas existan (por si se corre antes que main.py).
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # TODO 1: Leer los productos desde el archivo JSON.
        with open(RUTA_PRODUCTOS, encoding="utf-8") as archivo:
            datos = json.load(archivo)

        # Contar cuántos productos nuevos se agregan.
        cargados = 0

        # TODO 2: Recorrer los productos del archivo JSON.
        for item in datos:

            # Buscar la categoría por su nombre.
            categoria = (
                db.query(Categoria)
                .filter_by(nombre=item["categoria"])
                .first()
            )

            # Crear la categoría si todavía no existe.
            if categoria is None:
                categoria = Categoria(nombre=item["categoria"])
                db.add(categoria)

                # Obtener el ID de la categoría sin confirmar la transacción.
                db.flush()

            # Evitar insertar productos duplicados.
            producto_existente = (
                db.query(Producto)
                .filter_by(sku=item["sku"])
                .first()
            )

            if producto_existente is not None:
                continue

            # Crear el producto con los datos del JSON.
            producto = Producto(
                sku=item["sku"],
                marca=item["marca"],
                nombre=item["nombre"],
                precio=item["precio"],
                foto=item.get("foto"),
                stock=item["stock"],
                activo=item["activo"],
                categoria_id=categoria.id
            )

            db.add(producto)
            cargados += 1

        # TODO 3: Guardar los cambios en la base de datos.
        db.commit()

        # TODO 4: Mostrar la cantidad de productos nuevos.
        print(f"Se cargaron {cargados} productos nuevos.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    cargar_datos()
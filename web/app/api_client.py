"""
Cliente HTTP hacia el servicio 'api'.

Este módulo concentra todas las llamadas de red
hacia la API.
"""

import requests
from flask import current_app

TIMEOUT = 5  # Segundos máximos de espera por respuesta.


def obtener_productos(categoria_id=None):
    """Retorna la lista de productos desde la API."""

    url = f"{current_app.config['API_URL']}/productos/"

    # Agregar el filtro solo si se seleccionó una categoría.
    parametros = {}
    if categoria_id is not None:
        parametros = {"categoria_id": categoria_id}

    try:
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=TIMEOUT
        )

        if respuesta.status_code == 200:
            return respuesta.json()

        return []

    except requests.RequestException:
        return []


def obtener_producto(sku):
    """Retorna un producto por su SKU o None si no existe."""

    url = f"{current_app.config['API_URL']}/productos/{sku}"

    try:
        respuesta = requests.get(url, timeout=TIMEOUT)

        if respuesta.status_code == 200:
            return respuesta.json()

        return None

    except requests.RequestException:
        return None


def obtener_categorias():
    """Retorna la lista de categorías desde la API."""

    url = f"{current_app.config['API_URL']}/categorias/"

    try:
        respuesta = requests.get(url, timeout=TIMEOUT)

        if respuesta.status_code == 200:
            return respuesta.json()

        return []

    except requests.RequestException:
        return []
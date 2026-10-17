"""
Rutas del frontend.

CAMBIO CLAVE respecto al Taller 2: aquí NO hay consultas ORM.
Todo pasa por funciones de api_client, que hacen peticiones HTTP
al servicio 'api'.
"""

from flask import Blueprint, abort, render_template, request

from . import api_client

main = Blueprint("main", __name__)


@main.route("/")
def index():
    # Obtener el ID de la categoría seleccionada, si existe.
    categoria_id = request.args.get("categoria", type=int)

    # TODO 1: Obtener los productos desde la API.
    productos = api_client.obtener_productos(categoria_id)

    # TODO 2: Obtener las categorías desde la API.
    categorias = api_client.obtener_categorias()

    # TODO 3: Mostrar la página principal de la tienda.
    return render_template(
        "index.html",
        productos=productos,
        categorias=categorias,
        categoria_id=categoria_id
    )


@main.route("/producto/<sku>")
def detalle(sku):
    # TODO 4: Buscar el producto por su SKU mediante la API.
    producto = api_client.obtener_producto(sku)

    # TODO 5: Mostrar un error 404 si el producto no existe.
    if producto is None:
        abort(404)

    # TODO 6: Mostrar la página de detalle del producto.
    return render_template("detalle.html", producto=producto)


@main.route("/categorias")
def categorias():
    # TODO 7: Obtener las categorías desde la API.
    categorias = api_client.obtener_categorias()

    # TODO 8: Mostrar la página de categorías.
    return render_template("categorias.html", categorias=categorias)
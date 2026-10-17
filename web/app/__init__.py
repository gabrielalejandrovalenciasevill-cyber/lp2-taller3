"""
Application factory del frontend.

Este servicio obtiene los datos de la tienda a través de la API.
"""

from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    # Cargar la configuración de la aplicación.
    app.config.from_object(config_class)

    # Importar y registrar las rutas de la tienda.
    from .routes import main
    app.register_blueprint(main)

    return app
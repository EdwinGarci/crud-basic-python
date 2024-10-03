from flask import Flask

# Rutas
from .routes import ProductRoutes, IndexRoutes

app = Flask(__name__)

def init_app(config):
    # Configuracion
    app.config.from_object(config)

    # Registro de Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(ProductRoutes.main, url_prefix='/products')

    return app
from flask import Flask
from backend.api.categoria import CategoriaResource
from flask_restful import Api
from backend.config.db import db, ma, app

api = Api(app)

from backend.api.usuario import Usuario, ruta_usuarios
from backend.api.categoria import Categoria, ruta_categorias
from backend.api.animal import Animal, ruta_animales
from backend.api.historia import Historia, ruta_historias
from backend.api.favorito import Favorito, ruta_favoritos

app.register_blueprint(ruta_usuarios, url_prefix='/api')
app.register_blueprint(ruta_categorias, url_prefix='/api')
app.register_blueprint(ruta_animales, url_prefix='/api')
app.register_blueprint(ruta_historias, url_prefix='/api')
app.register_blueprint(ruta_favoritos, url_prefix='/api')
api.add_resource(CategoriaResource, '/categorias')

@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')

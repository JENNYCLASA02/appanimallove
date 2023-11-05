from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.categoria import Categoria, CategoriasSchema
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
import os 

parser = reqparse.RequestParser()
parser.add_argument('nombre', type=str, required=True)
parser.add_argument('imagen', type=str) 

UPLOAD_FOLDER = r'D:\Nueva carpeta (2)\UNIVERSIDAD 2023-2\MOVIL 2\CORTE 3\Intento1\assets'

class CategoriaResource(Resource):
    def post(self):
        args = parser.parse_args()
        nombre = args['nombre']
        imagen_url = args['imagen'] 
        nueva_categoria = Categoria(nombre=nombre, imagen_url=imagen_url)
        db.session.add(nueva_categoria)
        db.session.commit()
        return {'message': 'Categoría guardada con éxito'}, 201
    

ruta_categorias = Blueprint("ruta_categoria", __name__)

categoria_schema = CategoriasSchema()
categorias_schema = CategoriasSchema(many=True)

@ruta_categorias.route('/uploadimagen', methods=['POST'])
def upload_imagen():
    if 'imagen' not in request.files:
        return {'message': 'No se ha proporcionado ninguna imagen'}, 400

    imagen = request.files['imagen']
    
    if imagen.filename == '':
        return {'message': 'El nombre del archivo no está presente'}, 400

    if imagen:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        filename = secure_filename(imagen.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        imagen.save(filepath)

        imagen_url = f'/assets/{filename}'

        return {'imagen_url': imagen_url}, 200

@ruta_categorias.route('/categorias', methods=['GET'])
def categoria():
    resultall = Categoria.query.all() #Select * from Categorias
    resultado_categoria= categorias_schema.dump(resultall)
    return jsonify(resultado_categoria)

@ruta_categorias.route('/savecategoria', methods=['POST'])
def save():
    nombre = request.json['nombre']
    imagen_url = request.json['imagen_url'] 
    new_categoria = Categoria(nombre=nombre, imagen_url=imagen_url)
    db.session.add(new_categoria)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_categorias.route('/updatecategoria', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    imagen_url = request.json['imagen_url'] 
    categoria = Categoria.query.get(id)   
    if categoria :
        print(categoria) 
        categoria.nombre = nombre
        categoria.imagen_url = imagen_url
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"
    
@ruta_categorias.route('/deletecategoria/<id>', methods=['DELETE'])
def eliminar(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return {'message': 'Categoría eliminada con éxito'}, 200
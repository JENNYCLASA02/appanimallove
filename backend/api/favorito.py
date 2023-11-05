from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.favorito import Favorito, FavoritosSchema

ruta_favoritos = Blueprint("ruta_favorito", __name__)

favorito_schema = FavoritosSchema()
favoritos_schema = FavoritosSchema(many=True)

@ruta_favoritos.route('/favoritos', methods=['GET'])
def favorito():
    resultall = Favorito.query.all() #Select * from favorito
    resultado_favorito= favoritos_schema.dump(resultall)
    return jsonify(resultado_favorito)

@ruta_favoritos.route('/savefavorito', methods=['POST'])
def save():
    usuario = request.json['usuario']
    animal = request.json['animal']
    new_favorito = Favorito(usuario,animal)
    db.session.add(new_favorito)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_favoritos.route('/updatefavorito', methods=['PUT'])
def Update():
    id = request.json['id']
    usuario = request.json['usuario']
    animal = request.json['animal']
    favorito = Favorito.query.get(id)   
    if favorito :
        print(favorito) 
        favorito.usuario = usuario
        favorito.animal = animal
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_favoritos.route('/deletefavorito/<id>', methods=['DELETE'])
def eliminar(id):
    favorito = Favorito.query.get(id)
    db.session.delete(favorito)
    db.session.commit()
    return jsonify(favorito_schema.dump(favorito))
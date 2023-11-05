from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.historia import Historia, HistoriasSchema

ruta_historias = Blueprint("ruta_historia", __name__)

historia_schema = HistoriasSchema()
historias_schema = HistoriasSchema(many=True)

@ruta_historias.route('/historias', methods=['GET'])
def historia():
    resultall = Historia.query.all() #Select * from historia
    resultado_historia= historias_schema.dump(resultall)
    return jsonify(resultado_historia)

@ruta_historias.route('/savehistoria', methods=['POST'])
def save():
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    imagen_url = request.json ['imagen_url']
    new_historia = Historia(titulo,descripcion,imagen_url)
    db.session.add(new_historia)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_historias.route('/updatehistoria', methods=['PUT'])
def Update():
    id = request.json['id']
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    imagen_url = request.json ['imagen_url']
    historia = Historia.query.get(id)   
    if historia :
        print(historia) 
        historia.titulo = titulo
        historia.descripcion = descripcion
        historia.imagen_url = imagen_url
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_historias.route('/deletehistoria/<id>', methods=['DELETE'])
def eliminar(id):
    historia = Historia.query.get(id)
    db.session.delete(historia)
    db.session.commit()
    return jsonify(historia_schema.dump(historia))
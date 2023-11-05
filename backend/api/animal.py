from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.animal import Animal, AnimalesSchema

ruta_animales = Blueprint("ruta_animal", __name__)

animal_schema = AnimalesSchema()
animales_schema = AnimalesSchema(many=True)

@ruta_animales.route('/animales', methods=['GET'])
def animal():
    resultall = Animal.query.all() #Select * from animal
    resultado_animal= animales_schema.dump(resultall)
    return jsonify(resultado_animal)

@ruta_animales.route('/saveanimal', methods=['POST'])
def save():
    id = request.json['id']
    nombre = request.json['nombre']
    edad = request.json['edad']
    ubicacion = request.json['ubicacion']
    descripcion = request.json['descripcion']
    imagen_url = request.json['imagen_url']
    estado = request.json['estado']
    animalcategoria = request.json['animalcategoria']
    new_animal = Animal(id,nombre,edad,ubicacion,descripcion,imagen_url,estado,animalcategoria)
    db.session.add(new_animal)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_animales.route('/updateanimal', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    edad = request.json['edad']
    ubicacion = request.json['ubicacion']
    descripcion = request.json['descripcion']
    imagen_url = request.json['imagen_url']
    estado = request.json['estado']
    animalcategoria = request.json['animalcategoria']
    animal = Animal.query.get(id)   
    if animal :
        print(animal) 
        animal.id = id
        animal.nombre = nombre
        animal.edad = edad
        animal.ubicacion = ubicacion
        animal.descripcion = descripcion
        animal.imagen_url = imagen_url
        animal.estado = estado
        animal.animalcategoria = animalcategoria
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_animales.route('/deleteanimal/<id>', methods=['DELETE'])
def eliminar(id):
    animal = Animal.query.get(id)
    db.session.delete(animal)
    db.session.commit()
    return jsonify(animal_schema.dump(animal))
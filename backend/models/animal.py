from backend.config.db import  db, ma, app

class Animal(db.Model):
    __tablename__ = "tblanimal"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    ubicacion = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    imagen_url = db.Column(db.String(255))
    estado = db.Column(db.Boolean)
    animalcategoria = db.Column(db.Integer, db.ForeignKey('tblcategoria.id'))

    def __init__(self,nombre,edad,ubicacion,descripcion,imagen_url,estado,animalcategoria) :
       self.nombre = nombre
       self.edad = edad
       self.ubicacion = ubicacion
       self.descripcion = descripcion
       self.imagen_url = imagen_url
       self.estado = estado
       self.animalcategoria = animalcategoria

with app.app_context():
    db.create_all()

class AnimalesSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','edad','ubicacion','descripcion','imagen_url','estado','animalcategoria')
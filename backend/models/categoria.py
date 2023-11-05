from backend.config.db import  db, ma, app

class Categoria(db.Model):
    __tablename__ = "tblcategoria"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    imagen_url = db.Column(db.String(255))

    def __init__(self, nombre,imagen_url) :
       self.nombre = nombre
       self.imagen_url = imagen_url

with app.app_context():
    db.create_all()

class CategoriasSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','imagen_url')
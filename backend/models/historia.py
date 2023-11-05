from backend.config.db import  db, ma, app

class Historia(db.Model):
    __tablename__ = "tblhistoria"

    id = db.Column(db.Integer, primary_key =True)
    titulo = db.Column(db.String(50))
    descripcion = db.Column(db.String(250))
    imagen_url = db.Column(db.String(255))
    
    def __init__(self, titulo,descripcion,imagen_url) :
       self.titulo = titulo
       self.descripcion = descripcion
       self.imagen_url = imagen_url
       
with app.app_context():
    db.create_all()

class HistoriasSchema(ma.Schema):
    class Meta:
        fields = ('id','titulo','descripcion','imagen_url')
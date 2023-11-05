from backend.config.db import  db, ma, app

class Favorito(db.Model):
    __tablename__ = "tblfavorito"

    id = db.Column(db.Integer, primary_key =True)
    usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    animal = db.Column(db.Integer, db.ForeignKey('tblanimal.id'))
    
    def __init__(self,usuario,animal) :
       self.usuario = usuario
       self.animal = animal
       
with app.app_context():
    db.create_all()

class FavoritosSchema(ma.Schema):
    class Meta:
        fields = ('id','usuario','animal')
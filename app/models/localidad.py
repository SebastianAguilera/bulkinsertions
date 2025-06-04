from dataclasses import dataclass
from app import db
#from app.models.pais import Pais

@dataclass(init=False, repr=True, eq=True)
class Localidad(db.Model):
    __tablename__ = 'localidades'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo_postal = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(100), nullable=False)
    #pais_id = db.Column(db.Integer, db.ForeignKey('paises.id'), nullable=False)

    # Relación con Pais
   # pais = db.relationship('Pais', back_populates='localidades')

   
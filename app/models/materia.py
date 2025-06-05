from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    #plan = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer)
  
    especialidad_id = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)
    especialidad = db.relationship('Especialidad', back_populates='materias')

from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Orientacion(db.Model):
    _tablename_='orientaciones'
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    ##
    especialidad_id = db.Column(db.Integer, db.ForeignKey('especialidades.id'))
    especialidad = db.relationship('Especialidad')
    plan_id = db.Column(db.Integer, db.ForeignKey('planes.id'))
    plan = db.relationship('Plan')

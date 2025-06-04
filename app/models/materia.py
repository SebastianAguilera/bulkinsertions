from __future__ import annotations
from dataclasses import dataclass
from app import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.especialidad import Especialidad

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    plan = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer, nullable=False)
  
    especialidad_id = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)
    especialidad = db.relationship('Especialidad', back_populates='materias')

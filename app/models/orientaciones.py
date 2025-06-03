from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Orientaciones(db.Model):
    __tablename__='orientaciones'
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    plan: str = db.Column(db.String(100), nullable=False)
    especialidad: str = db.Column(db.String(100), nullable=False)
    
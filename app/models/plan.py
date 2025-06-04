from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__='planes'
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    #especialidad: str = db.Column(db.String(100), nullable=False)
from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Pais(db.Model):
  __tablename__ = 'paises'
  id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre: str = db.Column(db.String(100), nullable=False)
  
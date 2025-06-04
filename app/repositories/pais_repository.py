from app.models import Pais
from app import db

class PaisRepository:
    @staticmethod
    def crear_pais(pais: Pais):
        db.session.add(pais)
        db.session.commit()
        return pais
    
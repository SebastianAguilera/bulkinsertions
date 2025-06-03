from app.models import Orientaciones
from app import db

class OrientacionesRepository:

    @staticmethod
    def crear_orientacion(orientaciones: Orientaciones):
        db.session.add(orientaciones)
        db.session.commit()
        return orientaciones
    
from app.models import Orientacion
from app import db

class OrientacionRepository:

    @staticmethod
    def crear_orientacion(orientacion: Orientacion):
        db.session.add(orientacion)
        db.session.commit()
        return orientacion
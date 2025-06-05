from app.models import Orientaciones
from app import db

class OrientacionesRepository:

    @staticmethod
    def crear_orientacion(orientaciones: Orientaciones):
        db.session.add(orientaciones)
        db.session.commit()
        return orientaciones
    
    def insertar_masivo(datos: list[dict]):
        db.session.bulk_insert_mappings(Orientaciones, datos)
        db.session.commit()
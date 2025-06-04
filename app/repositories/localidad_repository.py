from app import db
from app.models import Localidad

class LocalidadRepository:
    @staticmethod
    def crear_localidad(localidad: Localidad):
        db.session.add(localidad)
        db.session.commit()
        return localidad
    
    @staticmethod
    def insertar_masivo(datos: list[dict]):
        db.session.bulk_insert_mappings(Localidad, datos)
        db.session.commit()
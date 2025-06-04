from app import db
from app.models import Universidad

class UniversidadRepository:
    @staticmethod
    def crear_universidad(universidad):
        db.session.add(universidad)
        db.session.commit()
        return universidad
    
    @staticmethod
    def insertar_masivo(datos: list[dict]):
        db.session.bulk_insert_mappings(Universidad, datos)
        db.session.commit()

   
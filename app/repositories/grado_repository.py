from app.models import Grado
from app import db

class GradoRepository:

    @staticmethod
    def crear_grado(grado: Grado):
        db.session.add(grado)
        db.session.commit()
        return grado
    
    @staticmethod
    def insertar_masivo(datos: list[dict]):
        db.session.bulk_insert_mappings(Grado, datos)
        db.session.commit()
from app import db
from app.models import Materia

class MateriaRepository:

    @staticmethod
    def crear_materia(materia):
        db.session.add(materia)
        db.session.commit()
        return materia

    @staticmethod
    def insertar_masivo(datos: list[dict]):
        if not datos:
            return 0  
        db.session.bulk_insert_mappings(Materia, datos)
        db.session.commit()
       

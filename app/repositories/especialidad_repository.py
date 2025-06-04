from app import db
from app.models import Especialidad

class EspecialidadRepository:
    @staticmethod
    def crear_especialidad(especialidad):
        db.session.add(especialidad)
        db.session.commit()
        return especialidad
    
    @staticmethod
    def insertar_masivo(datos: list[dict]):
        db.session.bulk_insert_mappings(Especialidad, datos)
        db.session.commit()

   
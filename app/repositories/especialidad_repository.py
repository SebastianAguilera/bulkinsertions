from app import db
from app.models import especialidad

class EspecialidadRepository:
    @staticmethod
    def crear_especialidad(especialidad):
        db.session.add(especialidad)
        db.session.commit()
        return especialidad

   
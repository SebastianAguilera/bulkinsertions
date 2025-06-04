
from app import db
from app.models import Materia

class MateriaRepository:

    @staticmethod
    def insertar_masivo(datos: list[dict]):
        try:
            materias = [Materia(**dato) for dato in datos]
            db.session.add_all(materias)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

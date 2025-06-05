from app import db
from app.models import Materia
from sqlalchemy.exc import IntegrityError

class MateriaRepository:

    @staticmethod
    def crear_materia(materia):
        db.session.add(materia)
        db.session.commit()
        return materia
    from sqlalchemy.exc import IntegrityError

    @staticmethod
    def insertar_masivo(datos):
        for dato in datos:
            try:
                dato['ano'] = int(dato['ano'])
            except (ValueError, TypeError):
                dato['ano'] = None  

            existente = db.session.query(Materia).filter_by(id=dato['id']).first()
            if existente:
                continue

            materia = Materia(**dato)
            db.session.add(materia)
        
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
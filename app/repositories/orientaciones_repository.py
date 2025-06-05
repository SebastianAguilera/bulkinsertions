from app.models import Orientacion
from app import db
from sqlalchemy.exc import IntegrityError 

class OrientacionesRepository:

    @staticmethod
    def crear_orientacion(orientaciones: Orientacion):
        db.session.add(orientaciones)
        db.session.commit()
        return orientaciones
    
    @staticmethod
    def insertar_masivo(datos):
        for dato in datos:

            existente = db.session.query(Orientacion).filter_by(id=dato['id']).first()
            if existente:
                continue

            orientacion = Orientacion(**dato)
            db.session.add(orientacion)
        
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
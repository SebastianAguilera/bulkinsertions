from app.models import Plan
from app import db
from sqlalchemy.exc import IntegrityError

class PlanRepository:

    @staticmethod
    def crear_plan(plan: Plan):
        db.session.add(plan)
        db.session.commit()
        return plan
    @staticmethod
    def insertar_masivo(datos):
        for dato in datos:
            existente = db.session.query(Plan).filter_by(id=dato['id']).first()
            if existente:
                continue

            plan = Plan(**dato)
            db.session.add(plan)
        
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
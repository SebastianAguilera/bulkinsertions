from app.models import Plan
from app import db

class PlanRepository:

    @staticmethod
    def crear_plan(plan: Plan):
        db.session.add(plan)
        db.session.commit()
        return plan
    @staticmethod
    def insertar_masivo(datos: list[dict]):
        db.session.bulk_insert_mappings(Plan, datos)
        db.session.commit()
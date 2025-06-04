from app.models import Plan
from app import db

class PlanRepository:

    @staticmethod
    def crear_plan(plan: Plan):
        db.session.add(plan)
        db.session.commit()
        return plan
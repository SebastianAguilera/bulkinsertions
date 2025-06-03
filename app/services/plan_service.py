from app.models import Plan
from app.repositories import PlanRepository

class PlanService:

    @staticmethod
    def crear_plan(plan: Plan):
        PlanRepository.crear_plan(plan)
        return plan
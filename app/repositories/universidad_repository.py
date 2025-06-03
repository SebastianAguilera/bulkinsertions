from app import db
from app.models import universidad

class UniversidadRepository:
    @staticmethod
    def crear_universidad(universidad):
        db.session.add(universidad)
        db.session.commit()
        return universidad

   
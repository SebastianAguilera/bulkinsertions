from app.models import Universidad
from app.repositories import UniversidadRepository

class UniversidadService:
    
    @staticmethod
    def crear_universidad(universidad):
        "crea una nueva universidad en la base de datos."
        UniversidadRepository.crear_universidad(universidad )
        return universidad
    
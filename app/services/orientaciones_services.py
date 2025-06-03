from app.models import Orientaciones
from app.repositories import OrientacionesRepository

class OrientacionesService:

    @staticmethod
    def crear_orientaciones(orientaciones: Orientaciones):
        OrientacionesRepository.crear_orientacion(orientaciones)
        return orientaciones
    

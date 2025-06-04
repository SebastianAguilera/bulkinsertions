from app.models import Orientacion
from app.repositories import OrientacionRepository

class OrientacionService:

    @staticmethod
    def crear_orientacion(orientacion: Orientacion):
        OrientacionRepository.crear_orientacion(orientacion)
        return orientacion
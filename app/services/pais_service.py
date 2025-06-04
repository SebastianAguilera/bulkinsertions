from app.models import Pais
from app.repositories import PaisRepository

class PaisService:
    @staticmethod
    def crear_pais(pais: Pais):
        PaisRepository.crear_pais(pais)
        return pais
    
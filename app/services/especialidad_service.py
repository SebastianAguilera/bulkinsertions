from app.models import especialidad
from app.repositories import EspecialidadRepository

class EspecialidadService:
    
    @staticmethod
    def crear_especialidad(especialidad: Especialidad):
        "crea una nueva especialidad en la base de datos."
        EspecialidadRepository.crear_especialidad(especialidad)
        return especialidad
    
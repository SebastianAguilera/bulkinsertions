from app.models import Facultad
from app import db


class FacultadRepository:
  @staticmethod
  def crear_facultad(facultad: Facultad):
    db.session.add(facultad)
    db.session.commit()
    return facultad
  
  @staticmethod
  def insertar_masivo(datos: list[dict]):
      db.session.bulk_insert_mappings(Facultad, datos)
      db.session.commit()
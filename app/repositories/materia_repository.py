from app import db
from app.models import Materia
from sqlalchemy.exc import IntegrityError

class MateriaRepository:

    @staticmethod
    def crear_materia(materia):
        db.session.add(materia)
        db.session.commit()
        return materia

    @staticmethod
    def insertar_masivo(materias_raw):
        
      nombres_existentes = {
          nombre for (nombre,) in db.session.query(Materia.nombre).all()
          }

      materias_filtradas = [
          m for m in materias_raw if m['nombre'] not in nombres_existentes
      ]

      try:
          db.session.bulk_insert_mappings(Materia, materias_filtradas)
          db.session.commit()
          print(f"Se insertaron {len(materias_filtradas)} materias.")
      except Exception as e:
          db.session.rollback()
          print(f"Error en la inserción masiva: {e}")

import os
import xml.etree.ElementTree as ET
from app.models import Materia
from app.repositories import MateriaRepository

class MateriaService:

    @staticmethod
    def crear_materia(materia):
        MateriaRepository.crear_materia(materia)
        return materia

    @staticmethod
    def insertar_masivo(ruta: str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            try:
                materia_id = item.findtext('id')
                nombre = item.findtext('nombre')
                plan = item.findtext('plan')
                ano = item.findtext('ano')
                especialidad_id = item.findtext('especialidad_id')

                if None in (materia_id, nombre, plan, ano, especialidad_id):
                    continue  # Salta ítems con campos faltantes

                datos.append({
                    'id': int(materia_id),
                    'nombre': nombre.strip(),
                    'plan': int(plan),
                    'ano': int(ano),
                    'especialidad_id': int(especialidad_id)
                })
            except Exception:
                continue  

        MateriaRepository.insertar_masivo(datos)

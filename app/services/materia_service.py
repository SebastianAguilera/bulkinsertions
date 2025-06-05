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
          materia_id = int(item.find('materia').text)
          nombre = item.find('nombre').text.strip()
          ano = item.find('ano').text 
          especialidad = int(item.find('especialidad').text)

          datos.append({'id': materia_id, 'nombre': nombre, 'ano': ano, 'especialidad_id': especialidad})

      MateriaRepository.insertar_masivo(datos)
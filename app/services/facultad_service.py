from app.models import Facultad
from app.repositories import FacultadRepository
import xml.etree.ElementTree as ET


class FacultadService:
  @staticmethod
  def crear_facultad(facultad: Facultad):
    return FacultadRepository.crear_facultad(facultad)
  
  @staticmethod
  def insertar_masivo(ruta: str):
      tree = ET.parse(ruta)
      root = tree.getroot()

      datos = []
      for item in root.findall('_expxml'):
          facultad_id = int(item.find('facultad').text)
          nombre = item.find('nombre').text.strip()
          datos.append({'id': facultad_id, 'nombre': nombre})

      FacultadRepository.insertar_masivo(datos)

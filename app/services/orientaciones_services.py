from app.models import Orientaciones
from app.repositories import OrientacionesRepository
import xml.etree.ElementTree as ET
import os

class OrientacionesService:

    @staticmethod
    def crear_orientaciones(orientaciones: Orientaciones):
        OrientacionesRepository.crear_orientacion(orientaciones)
        return orientaciones
    
    @staticmethod
    def insertar_masivo(ruta:str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            orientaciones_id = int(item.find('orientaciones').text)
            nombre = item.find('orientaciones').text.strip()
            datos.append({'id': orientaciones_id, 'nombre': nombre})

        OrientacionesRepository.insertar_masivo(datos)
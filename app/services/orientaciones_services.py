from app.models import Orientacion
from app.repositories import OrientacionesRepository
import xml.etree.ElementTree as ET
import os

class OrientacionService:

    @staticmethod
    def crear_orientaciones(orientaciones: Orientacion):
        OrientacionesRepository.crear_orientacion(orientaciones)
        return orientaciones
    
   
    @staticmethod
    def insertar_masivo(ruta:str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            orientaciones_id = int(item.find('orientacion').text)
            nombre = item.find('nombre').text.strip()
            datos.append({'id': orientaciones_id, 'nombre': nombre})

        OrientacionesRepository.insertar_masivo(datos)
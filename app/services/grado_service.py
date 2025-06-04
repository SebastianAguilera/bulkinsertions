from app.models import Grado
from app.repositories import GradoRepository
import xml.etree.ElementTree as ET
import os


class GradoService:

    @staticmethod
    def crear_grado(grado: Grado):
        GradoRepository.crear_grado(grado)
        return grado
    
    @staticmethod
    def insertar_masivo(ruta: str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            grado_id = int(item.find('grado').text)
            nombre = item.find('nombre').text.strip()
            datos.append({'id': grado_id, 'nombre': nombre})

        GradoRepository.insertar_masivo(datos)

    
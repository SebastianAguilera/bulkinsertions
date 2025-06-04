from app.models import Pais
from app.repositories import PaisRepository
import xml.etree.ElementTree as ET
import os


class PaisService:
    @staticmethod
    def crear_pais(pais: Pais):
        PaisRepository.crear_pais(pais)
        return pais
    
    @staticmethod
    def insertar_masivo(ruta:str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            pais_id = int(item.find('pais').text)
            nombre = item.find('nombre').text.strip()
            datos.append({'id': pais_id, 'nombre': nombre})

        PaisRepository.insertar_masivo(datos)
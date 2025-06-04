import os
from app.models import Universidad
import xml.etree.ElementTree as ET
from app.repositories import UniversidadRepository

ruta = os.path.join('archivados_xml', 'universidad.xml')

class UniversidadService:
    
    @staticmethod
    def crear_universidad(universidad):
        "crea una nueva universidad en la base de datos."
        UniversidadRepository.crear_universidad(universidad )
        return universidad
    
    
    @staticmethod
    def insertar_masivo(ruta: str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            universidad_id = int(item.find('universida').text)
            nombre = item.find('nombre').text.strip()
            datos.append({'id': universidad_id, 'nombre': nombre})

        UniversidadRepository.insertar_masivo(datos)
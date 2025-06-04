import os
from app.models import Especialidad
from app.repositories import EspecialidadRepository
import xml.etree.ElementTree as ET


ruta = os.path.join('archivados_xml', 'especialidades.xml')

class EspecialidadService:
    
    @staticmethod
    def crear_especialidad(especialidad: Especialidad):        
        "crea una nueva especialidad en la base de datos."
        EspecialidadRepository.crear_especialidad(especialidad)
        return especialidad

    @staticmethod
    def importar_desde_xml(ruta_archivo: str):
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        
        datos = []
        for item in root.findall('_expxml'):
            especialidad_id = int(item.find('especialidad').text)
            nombre = item.find('nombre').text.strip()
            datos.append({'id': especialidad_id, 'nombre': nombre})

        EspecialidadRepository.insertar_masivo(datos)
    
    @staticmethod
    def insertar_masivo(ruta: str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            especialidad_id = int(item.find('especialidad').text)
            nombre = item.find('nombre').text.strip()
            datos.append({'id': especialidad_id, 'nombre': nombre})

        EspecialidadRepository.insertar_masivo(datos)
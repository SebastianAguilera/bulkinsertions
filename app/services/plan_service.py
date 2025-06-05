from app.models import Plan
from app.repositories import PlanRepository
import xml.etree.ElementTree as ET
import os
import xml.etree.ElementTree as ET 
from app.models import Plan         
from app.repositories import PlanRepository


ruta = os.path.join('archivados_xml', 'planes.xml')

class PlanService:

    @staticmethod
    def crear_plan(plan: Plan):
        PlanRepository.crear_plan(plan)
        return plan

    @staticmethod
    def insertar_masivo(ruta: str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            materia = int(item.find('materia').text)
            nombre = item.find('nombre').text.strip()
            ano = int(item.find('ano').text)
            datos.append({'id': materia, 'nombre': nombre, 'ano': ano})

        PlanRepository.insertar_masivo(datos)
    

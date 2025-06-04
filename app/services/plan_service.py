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
            plan = int(item.find('plan').text)
            nombre = item.find('nombre').text.strip()
            datos.append({'plan': plan, 'nombre': nombre})

        PlanRepository.insertar_masivo(datos)
    

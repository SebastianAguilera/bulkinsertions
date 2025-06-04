from app.models import Plan
from app.repositories import PlanRepository
import xml.etree.ElementTree as ET
import os

ruta = os.path.join('archivados_xml', 'planes.xml')

class PlanService:

    @staticmethod
    def crear_plan(plan: Plan):
        PlanRepository.crear_plan(plan)
        return plan

    @staticmethod
    def importar_desde_xml(ruta_archivo: str):
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            grado_id = int(item.find('grado').text)
            nombre = item.find('nombre').text.strip()
            datos.append({'id': grado_id, 'nombre': nombre})

        PlanRepository.insertar_masivo(datos)
    
import unittest
from flask import current_app
from app import create_app
from app.models import Plan
from app.services import PlanService
from app import db
import os


class PlanTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_plan(self):
        plan = self.__crear_plan()
        self.assertEqual(plan.nombre, 'Nombre del plan')
        self.assertEqual(plan.id, 1)
        #self.assertEqual(plan.especialidad, 'Plan especialidad')

    

    def test_crear_plan(self):
        plan = self.__crear_plan()
        plan_guardado = PlanService.crear_plan(plan)
        self.assertIsNotNone(plan_guardado)
        self.assertIsNotNone(plan_guardado.id)
        self.assertIsNotNone(plan_guardado.id,1)
        self.assertEqual(plan_guardado.nombre, plan.nombre)
        #self.assertEqual(plan_guardado.especialidad, plan.especialidad)

    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "planes.xml")

        import xml.etree.ElementTree as ET
        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        PlanService.insertar_masivo(ruta)

        total_en_db = db.session.query(Plan).count()
        self.assertEqual(total_en_xml, total_en_db)

    def __crear_plan(self):
        plan = Plan()
        plan.id = 1
        plan.nombre = 'Nombre del plan'
        #plan.especialidad = 'Plan especialidad'
        return plan
    

if __name__ == '__main__':
    unittest.main()
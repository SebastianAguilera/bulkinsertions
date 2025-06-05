import unittest
import os
from flask import current_app
from app import create_app, db
from app.models import Orientacion, Especialidad, Plan
from app.services import OrientacionService,  EspecialidadService, PlanService

class OrientacionTestCase(unittest.TestCase):

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

    def test_orientacion(self):
        orientacion, especialidad, plan = self.__crear_orientacion()
        self.assertEqual(orientacion.nombre, 'nombre orientacion')
        ####
        self.assertEqual(orientacion.especialidad, especialidad)
        self.assertEqual(orientacion.plan, plan)

    def test_crear_orientacion(self):
        orientacion, especialidad, plan = self.__crear_orientacion()
        orientacion_guardada = OrientacionService.crear_orientaciones(orientacion)
        self.assertIsNotNone(orientacion_guardada)
        self.assertIsNotNone(orientacion_guardada.id)
        self.assertGreaterEqual(orientacion_guardada.id, 1)
        self.assertEqual(orientacion_guardada.nombre, orientacion.nombre)
        ###
        self.assertEqual(orientacion_guardada.especialidad, orientacion.especialidad)
        self.assertEqual(orientacion_guardada.especialidad_id, especialidad.id)
        self.assertIsInstance(orientacion_guardada.especialidad, Especialidad)

    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "orientaciones.xml")
        import xml.etree.ElementTree as ET
        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} orientaciones en el archivo.")
        OrientacionService.insertar_masivo(ruta)
        total_en_db = db.session.query(Orientacion).count()
        print(f"[DB] Se insertaron {total_en_db} orientaciones en la tabla grado.")

        orientaciones_dict = {}

        for item in root.findall('_expxml'):
            orientacion_id = item.find('orientacion')
            nombre = item.find('nombre')

            if orientacion_id is not None and nombre is not None:
                id_str = orientacion_id.text.strip()
                nombre_str = nombre.text.strip()
                
                if id_str not in orientaciones_dict:
                    orientaciones_dict[id_str] = nombre_str

        self.assertEqual(len(orientaciones_dict), total_en_db)


    

    def __crear_orientacion(self):
        especialidad = self.__crear_especialidad()
        especialidad_guardada = EspecialidadService.crear_especialidad(especialidad)
        plan = self.__crear_plan()
        orientacion = Orientacion()
        plan_guardado = PlanService.crear_plan(plan)        
        orientacion.nombre = 'nombre orientacion'
        orientacion.especialidad = especialidad_guardada
        orientacion.plan = plan_guardado
        return orientacion, especialidad, plan
    
    def __crear_especialidad(self):
        especialidad = Especialidad()
        especialidad.nombre = 'especialidad'
        return especialidad
    
    def __crear_plan(self):
        plan = Plan()
        plan.nombre = 'plan'
        return plan

if __name__ == '__main__':
    unittest.main()
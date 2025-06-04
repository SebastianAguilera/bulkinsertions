import unittest
from flask import current_app
from app import create_app
from app.models import Especialidad
from app.services import EspecialidadService
from app import db
import os

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
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
    
    def test_cart(self):
        especialidad = Especialidad()
        especialidad.nombre = "nombre"
        self.assertIsNotNone(especialidad)
        self.assertEqual(especialidad.nombre, "nombre")
        
    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "especialidades.xml")

        import xml.etree.ElementTree as ET
        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} especialidades en el archivo.")


        EspecialidadService.insertar_masivo(ruta)

        total_en_db = db.session.query(Especialidad).count()
        print(f"[DB] Se insertaron {total_en_db} registros en la tabla especialidad.")

        self.assertEqual(total_en_xml, total_en_db)
        
    def __crear_especialidad(self):
        especialidad = Especialidad()
        especialidad.nombre = 'especialidad'
        return especialidad



if __name__ == '__main__':
    unittest.main()
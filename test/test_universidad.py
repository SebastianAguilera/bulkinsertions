import unittest
import os
from app.services import UniversidadService
from flask import current_app
from app import create_app,db
from app.models import Universidad


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
        universidad = Universidad()
        universidad.nombre = "Universidad Tecnologica Nacional"
        self.assertIsNotNone(universidad)
        self.assertEqual(universidad.nombre, "Universidad Tecnologica Nacional")
        
    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "universidad.xml")

        import xml.etree.ElementTree as ET
        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} universidades en el archivo.")


        UniversidadService.insertar_masivo(ruta)

        total_en_db = db.session.query(Universidad).count()
        print(f"[DB] Se insertaron {total_en_db} registros en la tabla universidad.")

        self.assertEqual(total_en_xml, total_en_db)
        
    def __crear_universidad(self):
        universidad = Universidad()
        universidad.nombre = 'universidad'
        return universidad

if __name__ == '__main__':
    unittest.main()
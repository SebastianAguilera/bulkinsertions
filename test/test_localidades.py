import unittest
from flask import current_app
from app import create_app
from app.models import Localidad
from app.services import LocalidadService
from app import db
import os


class LocalidadTestCase(unittest.TestCase):
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

    def test_localidad(self):
        localidad = Localidad()
        localidad.nombre = "San Rafael"
        localidad.codigo_postal = "5600"
        localidad.id_provincia = 1
        self.assertIsNotNone(localidad)
        self.assertEqual(localidad.nombre, "San Rafael")
        self.assertEqual(localidad.codigo_postal, "5600")
        self.assertEqual(localidad.id_provincia, 1)
        
    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "localidades.xml")

        import xml.etree.ElementTree as ET
        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} localidades en el archivo.")

        LocalidadService.insertar_masivo(ruta)

        total_en_db = db.session.query(Localidad).count()
        print(f"[DB] Se insertaron {total_en_db} registros en la tabla localidad.")

        self.assertEqual(total_en_xml, total_en_db)


if __name__ == '__main__':
    unittest.main()

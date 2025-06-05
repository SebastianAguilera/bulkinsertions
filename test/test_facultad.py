import unittest
from flask import current_app
from app import create_app
from app.models import Facultad
from app.services import FacultadService
from app import db
import os
from app import db

class CargoTestCase(unittest.TestCase):

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
  
    def test_facultad(self):
        facultad = self.__crear_facultad()

        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre, 'facultad')

    def test_crear_facultad(self):
        facultad = self.__crear_facultad()
        facultad_guardada = FacultadService.crear_facultad(facultad)
        self.assertIsNotNone(facultad_guardada)
        self.assertIsNotNone(facultad_guardada.id)
        self.assertEqual(facultad_guardada.nombre, facultad.nombre)

    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "facultades.xml")

        import xml.etree.ElementTree as ET
        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} facultades en el archivo.")


        FacultadService.insertar_masivo(ruta)

        total_en_db = db.session.query(Facultad).count()
        print(f"[DB] Se insertaron {total_en_db} registros en la tabla facultades.")

        self.assertEqual(total_en_xml, total_en_db)

    def __crear_facultad(self):
        facultad = Facultad()
        facultad.nombre = 'facultad'
        return facultad

if __name__ == '__main__':
    unittest.main()



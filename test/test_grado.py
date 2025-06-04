import unittest
from flask import current_app
from app import create_app
from app.models import Grado
from app.services import GradoService
from app import db
import os

class GradoTestCase(unittest.TestCase):

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
  
    def test_grado(self):
        grado = self.__crear_grado()
        self.assertIsNotNone(grado)
        self.assertEqual(grado.nombre, 'grado') 

    def test_crear_grado(self):
        grado = self.__crear_grado()
        grado_guardado = GradoService.crear_grado(grado)
        self.assertIsNotNone(grado_guardado)
        self.assertIsNotNone(grado_guardado.id)
        self.assertEqual(grado_guardado.nombre, grado.nombre)

    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "grados.xml")

        import xml.etree.ElementTree as ET
        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} grados en el archivo.")


        GradoService.insertar_masivo(ruta)

        total_en_db = db.session.query(Grado).count()
        print(f"[DB] Se insertaron {total_en_db} registros en la tabla grado.")

        self.assertEqual(total_en_xml, total_en_db)

    def __crear_grado(self):
        grado = Grado()
        grado.nombre = 'grado'
        return grado

if __name__ == '__main__':
    unittest.main()


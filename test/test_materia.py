import unittest
import os
import xml.etree.ElementTree as ET
from flask import current_app
from app import create_app, db
from app.models import Materia, Especialidad

from app.services import MateriaService, EspecialidadService

class MateriaTestCase(unittest.TestCase):

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

    def test_materia(self):
        materia, especialidad = self.__crear_materia()
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, 'nombre materia')
        self.assertEqual(materia.ano, 1)
        self.assertEqual(materia.especialidad, especialidad)


    def test_materia_creation(self):
        materia, especialidad = self.__crear_materia()
        materia_guardada = MateriaService.crear_materia(materia)
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, 'nombre materia')
        self.assertEqual(materia.ano, 1)
        self.assertEqual(materia.especialidad, especialidad)
        self.assertEqual(materia.id, 1)
        
    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "materias.xml")
        rutaespecialidad = os.path.join("archiudos_xml", "especialidades.xml")

        EspecialidadService.insertar_masivo(rutaespecialidad)

        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} materias en el archivo.")

        MateriaService.insertar_masivo(ruta)


        total_en_db = db.session.query(Materia).count()
        print(f"[DB] Se insertaron {total_en_db} registros en la tabla materias.")

        self.assertEqual(total_en_xml, total_en_db)

    def __crear_especialidad(self):
        especialidad = Especialidad()
        especialidad.nombre = 'nombre especialidad'
        return especialidad


if __name__ == '__main__':
    unittest.main()

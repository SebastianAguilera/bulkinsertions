import unittest
import os
import xml.etree.ElementTree as ET
from flask import current_app
from app import create_app, db
from app.models import Materia, Especialidad

from app.services import MateriaService  

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

    def test_materia_creation(self):
        especialidad = self.__crear_especialidad('Matematicas')
        db.session.add(especialidad)
        db.session.commit()

        materia = Materia(
            nombre='Algebra',
            plan=88,
            ano=5,
            especialidad_id=especialidad.id
        )
        db.session.add(materia)
        db.session.commit()

        materia_db = Materia.query.filter_by(nombre='Algebra').first()
        self.assertIsNotNone(materia_db)
        self.assertEqual(materia_db.nombre, 'Algebra')
        self.assertEqual(materia_db.plan, 88)
        self.assertEqual(materia_db.ano, 5)
        self.assertEqual(materia_db.especialidad.nombre, 'Matematicas')

    def __crear_especialidad(self, nombre='Especialidad'):
        especialidad = Especialidad()
        especialidad.nombre = nombre
        return especialidad

    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "materias.xml")
      

        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} materias en el archivo.")

        MateriaService.insertar_masivo(ruta)

        total_en_db = db.session.query(Materia).count()
        print(f"[DB] Se insertaron {total_en_db} registros en la tabla materias.")

        self.assertEqual(total_en_xml, total_en_db)


if __name__ == '__main__':
    unittest.main()

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
        self.assertEqual(materia.nombre, 'materia')
        self.assertEqual(materia.ano, 1)
        self.assertEqual(materia.especialidad, especialidad)


    def test_materia_creation(self):
        materia, especialidad = self.__crear_materia()
        materia_guardada = MateriaService.crear_materia(materia)
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, 'materia')
        self.assertEqual(materia.ano, 1)
        self.assertEqual(materia.especialidad, especialidad)
        self.assertEqual(materia.id, 1)
        
    def test_insertar_masivo(self):
        ruta = os.path.join("archivados_xml", "materias.xml")
        rutaespecialidad = os.path.join("archivados_xml", "especialidades.xml")

        EspecialidadService.insertar_masivo(rutaespecialidad)

        tree = ET.parse(ruta)
        root = tree.getroot()
        total_en_xml = len(root.findall('_expxml'))
        print(f"[XML] Se detectaron {total_en_xml} materias en el archivo.")

        MateriaService.insertar_masivo(ruta)


        total_en_db = db.session.query(Materia).count()
        print(f"[DB] Se insertaron {total_en_db} registros en la tabla materias.")

        ####
        materias_dict = {}

        for item in root.findall('_expxml'):
            materia_id = item.find('materia')
            nombre = item.find('nombre')

            if materia_id is not None and nombre is not None:
                id_str = materia_id.text.strip()
                nombre_str = nombre.text.strip()
                
                if id_str not in materias_dict:
                    materias_dict[id_str] = nombre_str

        print(f'Total de materias únicas: {len(materias_dict)}')
        
        self.assertEqual(len(materias_dict), total_en_db)

    def __crear_materia(self):
        materia = Materia()
        materia.nombre= 'materia'
        materia.ano = 1

        especialidad = Especialidad()
        especialidad.nombre = 'especialidad'
        especialidad_guardada = EspecialidadService.crear_especialidad(especialidad)
        materia.especialidad = especialidad_guardada

        return materia, especialidad

if __name__ == '__main__':
    unittest.main()

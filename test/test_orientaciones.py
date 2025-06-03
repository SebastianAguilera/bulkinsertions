import unittest
from flask import current_app
from app import create_app, db
from app.models import Orientaciones
from app.services import OrientacionesService

class OrientacionesTestCase(unittest.TestCase):

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

    def test_orientaciones(self):
        orientaciones = self.__crear_orientaciones()
        self.assertEqual(orientaciones.nombre, 'nombre orientacion')
        self.assertEqual(orientaciones.plan, 'nombre plan')
        self.assertEqual(orientaciones.especialidad, 'nombre especialidad')

    def test_crear_orientaciones(self):
        orientaciones = self.__crear_orientaciones()
        orientaciones_guardada = OrientacionesService.crear_orientaciones(orientaciones)
        self.assertIsNotNone(orientaciones_guardada)
        self.assertIsNotNone(orientaciones_guardada.id)
        self.assertGreaterEqual(orientaciones_guardada.id, 1)
        self.assertEqual(orientaciones_guardada.nombre, orientaciones.nombre)
        self.assertEqual(orientaciones_guardada.plan, orientaciones.plan)
        self.assertEqual(orientaciones_guardada.especialidad, orientaciones.especialidad)

    def __crear_orientaciones(self):
        orientaciones = Orientaciones()
        orientaciones.nombre = 'nombre orientacion'
        orientaciones.plan = 'nombre plan'
        orientaciones.especialidad = 'nombre especialidad'
        return orientaciones

if __name__ == '__main__':
    unittest.main()

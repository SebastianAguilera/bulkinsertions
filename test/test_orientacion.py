import unittest
from flask import current_app
from app import create_app, db
from app.models import Orientacion
from app.services import OrientacionService

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
        orientacion = self.__crear_orientacion()
        self.assertEqual(orientacion.nombre, 'nombre orientacion')
        #self.assertEqual(orientacion.plan, 'nombre plan')
        #self.assertEqual(orientacion.especialidad, 'nombre especialidad')

    def test_crear_orientacion(self):
        orientacion = self.__crear_orientacion()
        orientacion_guardada = OrientacionService.crear_orientacion(orientacion)
        self.assertIsNotNone(orientacion_guardada)
        self.assertIsNotNone(orientacion_guardada.id)
        self.assertGreaterEqual(orientacion_guardada.id, 1)
        self.assertEqual(orientacion_guardada.nombre, orientacion.nombre)
        #self.assertEqual(orientacion_guardada.plan, orientacion.plan)
        #self.assertEqual(orientacion_guardada.especialidad, orientacion.especialidad)

    def __crear_orientacion(self):
        orientacion = Orientacion()
        orientacion.nombre = 'nombre orientacion'
        #orientacion.plan = 'nombre plan'
        #orientacion.especialidad = 'nombre especialidad'
        return orientacion

if __name__ == '__main__':
    unittest.main()
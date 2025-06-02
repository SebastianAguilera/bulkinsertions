import unittest
from flask import current_app
from app import create_app
from app.models import Materia
#from app.models import Especialidad

class CargoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_materia(self):
        materia = Materia()
        materia.nombre = 'Algebra'
       # materia.especialidad = Especialidad(nombre='Matematicas')
        materia.plan = 88
        materia.ano = 5

        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, 'Algebra')
        #self.assertEqual(materia.especialidad.nombre, 'Matematicas')
        self.assertEqual(materia.plan, 88)
        self.assertEqual(materia.ano, 5)
if __name__ == '__main__':
    unittest.main()


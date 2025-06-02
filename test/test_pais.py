import unittest
from flask import current_app
from app import create_app
from app.models import Pais

class CargoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_pais(self):
        pais = Pais()
        pais.nombre ='Argentina'

        self.assertIsNotNone(pais)
        self.assertEqual(pais.nombre, 'Argentina')

if __name__ == '__main__':
    unittest.main()



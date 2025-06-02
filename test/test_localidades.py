import unittest
from flask import current_app
from app import create_app
from app.models import Localidad
#from app.models import Pais


class CargoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
  
    def test_localidad(self):
        localidad= Localidad()
        localidad.nombre = 'ciudad'
        localidad.codigo_postal = 5600
        localidad.provincia = 'mendoza'
       # localidad.pais = Pais(nombre='Argentina')

        self.assertIsNotNone(localidad)
        self.assertEqual(localidad.nombre, 'ciudad')
        self.assertEqual(localidad.codigo_postal, 5600) 
        self.assertEqual(localidad.provincia, 'mendoza')   
       # self.assertEqual(localidad.pais.nombre, 'Argentina')

if __name__ == '__main__':
    unittest.main()



import unittest
from flask import current_app
from app import create_app
from app.models import Pais
from app.services import PaisService
from app import db

class PaisTestCase(unittest.TestCase):

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
  
    def test_pais(self):
        pais = self.__crear_pais()
        self.assertEqual(pais.nombre, 'Argentina')

    def test_crear_pais(self):
        pais = self.__crear_pais()
        pais_guardado = PaisService.crear_pais(pais)
        self.assertIsNotNone(pais_guardado)
        self.assertIsNotNone(pais_guardado.id)
        self.assertIsNotNone(pais_guardado.id, 1)
        self.assertIsNotNone(pais_guardado. nombre, pais.nombre)

    def __crear_pais(self):
        pais = Pais()
        pais.nombre ='Argentina'
        return pais

if __name__ == '__main__':
    unittest.main()



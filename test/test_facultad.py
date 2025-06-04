import unittest
from flask import current_app
from app import create_app
from app.models import Facultad
from app import db

class CargoTestCase(unittest.TestCase):

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
  
    def test_facultad(self):
        facultad = Facultad()
        facultad.nombre = 'facultad'

        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre, 'facultad')

if __name__ == '__main__':
    unittest.main()



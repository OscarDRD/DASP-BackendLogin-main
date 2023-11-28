import unittest
from flask import jsonify
#from src.app import app
from app.Routes.CountryRoutes import handleCountryById

class TestCountryRoutes(unittest.TestCase):
    def test_handleCountryById_get_existing_country(self):
        with app.test_request_context('/country/1', method='GET'):
            response = handleCountryById(1)
            self.assertEqual(response[1], 200)
            self.assertEqual(response[0].json, {'id': 1, 'name': 'Country Name'})

    def test_handleCountryById_get_nonexistent_country(self):
        with app.test_request_context('/country/999', method='GET'):
            response = handleCountryById(999)
            self.assertEqual(response[1], 404)
            self.assertEqual(response[0].json, {'message': 'Country no encontrado'})

    def test_handleCountryById_put_existing_country(self):

        with app.test_request_context('/country/1', method='PUT', json={'name': 'New Country Name'}):
            response = handleCountryById(1)
            self.assertEqual(response[1], 200)
            self.assertEqual(response[0].json, {'message': 'Country actualizado con éxito'})

    def test_handleCountryById_put_nonexistent_country(self):
        with app.test_request_context('/country/999', method='PUT', json={'name': 'New Country Name'}):
            response = handleCountryById(999)
            self.assertEqual(response[1], 404)
            self.assertEqual(response[0].json, {'message': 'Country no encontrado'})

    def test_handleCountryById_delete_existing_country(self):
        with app.test_request_context('/country/1', method='DELETE'):
            response = handleCountryById(1)
            self.assertEqual(response[1], 200)
            self.assertEqual(response[0].json, {'message': 'Country eliminado con éxito'})

    def test_handleCountryById_delete_nonexistent_country(self):
        with app.test_request_context('/country/999', method='DELETE'):
            response = handleCountryById(999)
            self.assertEqual(response[1], 404)
            self.assertEqual(response[0].json, {'message': 'Country no encontrado'})

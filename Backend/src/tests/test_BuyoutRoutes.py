import unittest
from flask import jsonify
from app.Routes.BuyoutRoutes import handleBuyoutById

class TestBuyoutRoutes(unittest.TestCase):
    def test_handleBuyoutById_get_existing_buyout(self):
        with app.test_request_context('/buyout/1', method='GET'):
            response = handleBuyoutById(1)
            self.assertEqual(response[1], 200)
            self.assertEqual(response[0].json, {
                'buyouts': {'id': 1, 'name': 'Buyout Name'},
                'buyoutsDomains': [{'id': 1, 'name': 'Domain Name'}],
                'buyoutsHosting': [{'id': 1, 'name': 'Hosting Name'}],
                'costDomains': 100,
                'costHostings': 200,
                'totalCost': 300
            })

    def test_handleBuyoutById_get_nonexistent_buyout(self):
        with app.test_request_context('/buyout/999', method='GET'):
            response = handleBuyoutById(999)
            self.assertEqual(response[1], 404)
            self.assertEqual(response[0].json, {'message': 'Buyout no encontrado'})

    def test_handleBuyoutById_put_existing_buyout(self):
        with app.test_request_context('/buyout/1', method='PUT', json={'name': 'New Buyout Name'}):
            response = handleBuyoutById(1)
            self.assertEqual(response[1], 200)
            self.assertEqual(response[0].json, {'message': 'Buyout actualizado con éxito'})

    def test_handleBuyoutById_put_nonexistent_buyout(self):
        with app.test_request_context('/buyout/999', method='PUT', json={'name': 'New Buyout Name'}):
            response = handleBuyoutById(999)
            self.assertEqual(response[1], 404)
            self.assertEqual(response[0].json, {'message': 'Buyout no encontrado'})

    def test_handleBuyoutById_delete_existing_buyout(self):
        with app.test_request_context('/buyout/1', method='DELETE'):
            response = handleBuyoutById(1)
            self.assertEqual(response[1], 200)
            self.assertEqual(response[0].json, {'message': 'Buyout eliminado con éxito'})

    def test_handleBuyoutById_delete_nonexistent_buyout(self):
        with app.test_request_context('/buyout/999', method='DELETE'):
            response = handleBuyoutById(999)
            self.assertEqual(response[1], 404)
            self.assertEqual(response[0].json, {'message': 'Buyout no encontrado'})
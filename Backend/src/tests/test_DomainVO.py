import unittest
from app.Models.DomainVO import Domain

class TestDomainModels(unittest.TestCase):
    def test_to_JSON(self):
        domain = Domain(name='example.com', distributor_id=1, buyout_id=1, costDomain=10)
        expected_json = {
            'id': None,
            'name': 'example.com',
            'costDomain': 10,
            'distributor_id': 1,
            'buyout_id': 1
        }
        self.assertEqual(domain.to_JSON(), expected_json)

    def test_from_JSON(self):
        domain = Domain(name='example.com', distributor_id=1, buyout_id=1, costDomain=10)
        data = {
            'name': 'newexample.com',
            'costDomain': 20,
            'distributor_id': 2,
            'buyout_id': 2
        }
        domain.from_JSON(data)
        self.assertEqual(domain.name, 'newexample.com')
        self.assertEqual(domain.costDomain, 20)
        self.assertEqual(domain.distributor_id, 2)
        self.assertEqual(domain.buyout_id, 2)

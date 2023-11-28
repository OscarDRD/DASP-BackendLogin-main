import unittest
from app.Services.HostingDAO import HostingDAO

class TestHostingDAO(unittest.TestCase):
    def test_createHosting_with_valid_data(self):
        data = {'name': 'example.com', 'plan': 'basic'}
        id = 1
        result = HostingDAO.createHosting(data, id)
        self.assertIsInstance(result, Hosting)
        self.assertEqual(result.name, 'example.com')
        self.assertEqual(result.plan, 'basic')

    def test_createHosting_with_invalid_data(self):
        data = {'name': '', 'plan': 'basic'}
        id = 1
        result = HostingDAO.createHosting(data, id)
        self.assertEqual(result, {'error': 'Ocurrió un error al crear el dominio.'})

    def test_getHostings(self):
        result = HostingDAO.getHostings()
        self.assertIsInstance(result, list)

    def test_getHostingById_with_existing_id(self):
        id = 1
        result = HostingDAO.getHostingById(id)
        self.assertIsInstance(result, Hosting)
        self.assertEqual(result.id, 1)

    def test_getHostingById_with_nonexistent_id(self):
        id = 999
        result = HostingDAO.getHostingById(id)
        self.assertIsNone(result)

    def test_updateHosting_with_existing_id(self):
        id = 1
        data = {'name': 'updated.com', 'plan': 'premium'}
        result = HostingDAO.updateHosting(id, data)
        self.assertIsInstance(result, dict)
        self.assertEqual(result['name'], 'updated.com')
        self.assertEqual(result['plan'], 'premium')

    def test_updateHosting_with_nonexistent_id(self):
        id = 999
        data = {'name': 'updated.com', 'plan': 'premium'}
        result = HostingDAO.updateHosting(id, data)
        self.assertFalse(result)

    def test_deleteHosting_with_existing_id(self):
        id = 1
        result = HostingDAO.deleteHosting(id)
        self.assertIsInstance(result, Hosting)
        self.assertEqual(result.id, 1)

    def test_deleteHosting_with_nonexistent_id(self):
        id = 999
        result = HostingDAO.deleteHosting(id)
        self.assertIsInstance(result, Exception)

    def test_getHostingPlan(self):
        hosting = Hosting(name='example.com', plan='basic')
        result = HostingDAO.getHostingPlan(hosting)
        self.assertEqual(result, 'basic')

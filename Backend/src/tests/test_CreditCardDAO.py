import unittest
from app.Services.CreditCardDAO import CreditCardDAO

class TestCreditCardDAO(unittest.TestCase):
    def test_createCreditCard(self):
        data = {'number': '1234567890', 'name': 'John Doe'}
        result = CreditCardDAO.createCreditCard(data)
        self.assertIsNotNone(result)
        self.assertEqual(result.number, '1234567890')
        self.assertEqual(result.name, 'John Doe')

    def test_getCreditCards(self):
        result = CreditCardDAO.getCreditCards()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

    def test_getCreditCardById_existing_card(self):
        result = CreditCardDAO.getCreditCardById(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.id, 1)

    def test_getCreditCardById_nonexistent_card(self):
        result = CreditCardDAO.getCreditCardById(999)
        self.assertIsNone(result)

    def test_updateCreditCard_existing_card(self):
        data = {'number': '9876543210', 'name': 'Jane Doe'}
        result = CreditCardDAO.updateCreditCard(1, data)
        self.assertIsNotNone(result)
        self.assertEqual(result['number'], '9876543210')
        self.assertEqual(result['name'], 'Jane Doe')

    def test_updateCreditCard_nonexistent_card(self):
        data = {'number': '9876543210', 'name': 'Jane Doe'}
        result = CreditCardDAO.updateCreditCard(999, data)
        self.assertFalse(result)

    def test_deleteCreditCard_existing_card(self):
        result = CreditCardDAO.deleteCreditCard(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.id, 1)

    def test_deleteCreditCard_nonexistent_card(self):
        result = CreditCardDAO.deleteCreditCard(999)
        self.assertIsNone(result)

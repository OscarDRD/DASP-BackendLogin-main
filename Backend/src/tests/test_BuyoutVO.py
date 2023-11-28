import unittest
from app.Models.BuyoutVO import Buyout

class TestBuyout(unittest.TestCase):
    def setUp(self):
        self.buyout = Buyout(user_id=1, pay_plan_id=1, status='Pending')

    def test_to_JSON(self):
        expected_json = {
            'id': None,
            'user_id': 1,
            'pay_plan_id': 1,
            'status': 'Pending'
        }
        self.assertEqual(self.buyout.to_JSON(), expected_json)

    def test_from_JSON(self):
        data = {
            'user_id': 2,
            'pay_plan_id': 2,
            'status': 'Approved'
        }
        self.buyout.from_JSON(data)
        self.assertEqual(self.buyout.user_id, 2)
        self.assertEqual(self.buyout.pay_plan_id, 2)
        self.assertEqual(self.buyout.status, 'Approved')

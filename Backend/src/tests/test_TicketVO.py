import unittest
from app.Models.TicketVO import Ticket

class TestTicket(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket(
            description='Test Description',
            message='Test Message',
            services='Test Services',
            state=True,
            priority=1,
            user_id=1,
            user_it_id=2
        )

    def test_to_JSON(self):
        expected_json = {
            'id': None,
            'description': 'Test Description',
            'message': 'Test Message',
            'services': 'Test Services',
            'state': True,
            'priority': 1,
            'user_id': 1,
            'user_it_id': 2
        }
        self.assertEqual(self.ticket.to_JSON(), expected_json)

    def test_from_JSON(self):
        data = {
            'description': 'Updated Description',
            'message': 'Updated Message',
            'services': 'Updated Services',
            'state': False,
            'priority': 2,
            'user_id': 3,
            'user_it_id': 4
        }
        self.ticket.from_JSON(data)
        self.assertEqual(self.ticket.description, 'Updated Description')
        self.assertEqual(self.ticket.message, 'Updated Message')
        self.assertEqual(self.ticket.services, 'Updated Services')
        self.assertEqual(self.ticket.state, False)
        self.assertEqual(self.ticket.priority, 2)
        self.assertEqual(self.ticket.user_id, 3)
        self.assertEqual(self.ticket.user_it_id, 4)

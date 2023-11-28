import unittest
from app.Models.UserVO import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(
            name='John Doe',
            email='johndoe@example.com',
            password='password123',
            phone=1234567890,
            idDocument='ABC123',
            document_type='Passport',
            country_id=1,
            jobTittle='Software Engineer',
            direction='123 Main St',
            payMode_id=1,
            rol_id=1
        )

    def test_to_JSON(self):
        expected_json = {
            'id': None,
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone': 1234567890,
            'idDocument': 'ABC123',
            'document_type': 'Passport',
            'country_id': 1,
            'jobTittle': 'Software Engineer',
            'direction': '123 Main St',
            'payMode_id': 1,
            'rol_id': 1,
            'password': 'password123'
        }
        self.assertEqual(self.user.to_JSON(), expected_json)

    def test_from_JSON(self):
        data = {
            'name': 'Jane Smith',
            'email': 'janesmith@example.com',
            'phone': 9876543210,
            'idDocument': 'XYZ789',
            'document_type': 'Driver License',
            'country_id': 2,
            'jobTittle': 'Product Manager',
            'direction': '456 Elm St',
            'payMode_id': 2,
            'rol_id': 2
        }
        self.user.from_JSON(data)
        self.assertEqual(self.user.name, 'Jane Smith')
        self.assertEqual(self.user.email, 'janesmith@example.com')
        self.assertEqual(self.user.phone, 9876543210)
        self.assertEqual(self.user.idDocument, 'XYZ789')
        self.assertEqual(self.user.document_type, 'Driver License')
        self.assertEqual(self.user.country_id, 2)
        self.assertEqual(self.user.jobTittle, 'Product Manager')
        self.assertEqual(self.user.direction, '456 Elm St')
        self.assertEqual(self.user.payMode_id, 2)
        self.assertEqual(self.user.rol_id, 2)

    def test_checkPassword(self):
        hashed_password = User.convertPassword('password123')
        self.assertTrue(User.checkPassword(hashed_password, 'password123'))
        self.assertFalse(User.checkPassword(hashed_password, 'wrongpassword'))

    def test_hashPassword(self):
        self.user.hashPassword()
        self.assertNotEqual(self.user.password, 'password123')

    def test_validateInformationByRol(self):
        # Test for rol_id = 1
        self.assertTrue(self.user.validateInformationByRol())

        # Test for rol_id = 2 with incomplete jobTittle
        self.user.rol_id = 2
        self.user.jobTittle = None
        self.assertFalse(self.user.validateInformationByRol())

        # Test for rol_id = 3
        self.user.rol_id = 3
        self.assertTrue(self.user.validateInformationByRol())

        # Test for empty rol_id
        self.user.rol_id = None
        self.assertTrue(self.user.validateInformationByRol())

        # Test for invalid rol_id
        self.user.rol_id = 4
        self.assertTrue(self.user.validateInformationByRol())


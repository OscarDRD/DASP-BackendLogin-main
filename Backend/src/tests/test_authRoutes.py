import unittest
from flask import jsonify
from app.Routes.authRoutes import login

class TestAuthRoutes(unittest.TestCase):
    def test_login_with_valid_credentials(self):
        with app.test_request_context('/login/', method='POST', json={'email': 'test@example.com', 'password': 'password123'}):
            response = login()
            self.assertEqual(response[1], 200)
            self.assertEqual(response[0].json, {'mensaje': 'Inicio de sesión exitoso', 'Token': 'generated_token', 'Name': 'John Doe', 'Rol': 'admin', 'id': 1})

    def test_login_with_invalid_password(self):
        with app.test_request_context('/login/', method='POST', json={'email': 'test@example.com', 'password': 'wrongpassword'}):
            response = login()
            self.assertEqual(response[1], 401)
            self.assertEqual(response[0].json, {'mensaje': 'Error de autenticación: contraseña incorrecta'})

    def test_login_with_invalid_user(self):
        with app.test_request_context('/login/', method='POST', json={'email': 'nonexistent@example.com', 'password': 'password123'}):
            response = login()
            self.assertEqual(response[1], 404)
            self.assertEqual(response[0].json, {'message': 'Usuario no encontrado'})

    def test_login_with_invalid_method(self):
        with app.test_request_context('/login/', method='GET'):
            response = login()
            self.assertEqual(response[1], 405)
            self.assertEqual(response[0].json, {'message': 'Method Not Allowed'})

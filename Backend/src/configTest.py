class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # Usa una base de datos de prueba separada
    WTF_CSRF_ENABLED = False
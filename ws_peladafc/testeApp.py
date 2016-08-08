import unittest
from app import app


class TddInApp(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test"""
        self.app = app.test_client()

    def test_get_usuarios(self):
        rs =  self.app.get('/user/', follow_redirects=True)
        self.assertIsNone('Lista vazia!', rs)


if __name__ == '__main__':
    unittest.main()
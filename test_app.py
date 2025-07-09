import unittest
import json
from app import app, db

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_add_user(self):
        response = self.client.post('/users', json={"name": "Alice"})
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        self.client.post('/users', json={"name": "Bob"})
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)

if __name__ == "__main__":
    unittest.main()

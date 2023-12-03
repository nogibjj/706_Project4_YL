import unittest
from app import app
import urllib.parse

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to MovieRec", response.data)

    def test_recommend_title(self):
        response = self.app.get("/recommend?title=Known Title")
        self.assertEqual(response.status_code, 200)

    def test_recommend_director(self):
        # URL encode the author name
        director_name = "Christopher Nolan"
        encoded_director_name = urllib.parse.quote_plus(director_name)

        # make the test request
        response = self.app.get(f"/recommend?directors={encoded_director_name}")

        # check if response status code is 200
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
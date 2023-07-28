import unittest
from my_flask_app import app

class FlaskAppTestCase(unittest.TestCase):
    """
    Test case for testing the Flask app.
    """

    def setUp(self):
        """
        Set up the test client before each test.
        """
        self.client = app.test_client()

    def test_add_book_success(self):
        """
        Test adding a book with valid data.
        """
        book_data = {
            'title': 'Sample Book',
            'author': 'John Doe',
            'pages': '200',
            'genre': 'Fiction',
            'isbn': '1234567890'
        }
        response = self.client.get('/add_book', query_string=book_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book added successfully", response.data)

    def test_add_book_invalid_data(self):
        """
        Test adding a book with incomplete data.
        """
        book_data = {
            'title': 'Sample Book',
            'author': 'John Doe',
            'pages': '200'
        }
        response = self.client.get('/add_book', query_string=book_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invalid data. Please provide all book details.", response.data)

if __name__ == '__main__':
    unittest.main()


from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book

class BookAPITestCase(TestCase):
    """ Test suite for Book API endpoints """

    def setUp(self):
        """ Set up test data before running each test """
        self.client = APIClient()

        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create test book instances
        self.book1 = Book.objects.create(title="Django for Beginners", author="William Vincent", publication_year=2020)
        self.book2 = Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2019)

        # Login the test user
        self.client.login(username='testuser', password='testpass')

        # API Endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book1.id}/"

    def test_list_books(self):
        """ Test retrieving a list of books """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)  # Ensure at least 2 books are returned

    def test_get_book_detail(self):
        """ Test retrieving a single book """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        """ Test creating a new book """
        data = {"title": "New Book", "author": "John Doe", "publication_year": 2022}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # Ensure a new book is added

    def test_update_book(self):
        """ Test updating an existing book """
        data = {"title": "Updated Title", "author": "William Vincent", "publication_year": 2020}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """ Test deleting a book """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Ensure book is deleted

    def test_filter_books_by_author(self):
        """ Test filtering books by author """
        response = self.client.get(f"{self.list_url}?author=Eric Matthes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """ Test searching books by title """
        response = self.client.get(f"{self.list_url}?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """ Test ordering books by publication year (ascending) """
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data
        self.assertTrue(books[0]['publication_year'] <= books[1]['publication_year'])

    def test_authentication_required_for_create(self):
        """ Ensure unauthenticated users cannot create books """
        self.client.logout()
        data = {"title": "Unauthorized Book", "author": "Hackerman", "publication_year": 2025}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Permission denied

    def test_authentication_required_for_delete(self):
        """ Ensure unauthenticated users cannot delete books """
        self.client.logout()
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

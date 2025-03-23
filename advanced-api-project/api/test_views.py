from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token  # For token-based authentication
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create an Author instance
        self.author = Author.objects.create(name="Test Author")
        
        # Create a Book instance
        self.book_data = {
            "title": "Test Book",
            "author": self.author.id,  # Foreign key reference
            "publication_year": 2023
        }
        self.book = Book.objects.create(
            title=self.book_data["title"],
            author=self.author,
            publication_year=self.book_data["publication_year"]
        )
        
        # Create a test user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")  # Login with the test user
        
        # Alternatively, for token authentication:
        # self.token = Token.objects.create(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_book(self):
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_create_book(self):
        new_book_data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.post("/api/books/", new_book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], new_book_data["title"])

    def test_update_book(self):
        updated_book_data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2024
        }
        response = self.client.put(f"/api/books/{self.book.id}/", updated_book_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], updated_book_data["title"])

    def test_delete_book(self):
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

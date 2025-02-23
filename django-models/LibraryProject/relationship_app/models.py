from django.db import models


# Author model.
class Author (models.Model):
    name = models.CharField(max_length=100)


# Book model
class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Book')


# Library model
class Library (models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')


# Librarian model
class Librarian (models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


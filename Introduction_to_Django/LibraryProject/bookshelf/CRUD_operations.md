>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
>>> book.title="Nineteen Eighty-Four"
>>> book.save()
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> print(Book.objects.all())
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
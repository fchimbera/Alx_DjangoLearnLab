# Delete Operation

```python
from bookshelf.models import Book
book.delete()
print(Book.objects.all())  # Expected output: <QuerySet []>

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import filters

# BookListView is a view that will return a list of all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filterset fields is used to filter the queryset using the filterset_fields attribute
    filterset_fields = ['title', 'author', 'publication_year']

    # Search filter is used to search the queryset using the search_fields attribute
    search_fields = ['title', 'author']

    # Ordering filter is used to order the queryset using the ordering_fields attribute
    ordering_fields = ['title', 'publication_year']

# BookDetailView is a view that will return a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

# BookCreateView is a view that will create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get the publication year from the serializer data
        publication_year = serializer.validated_data.get('publication_year')
        current_year = datetime.now().year

        if publication_year and publication_year > current_year:
            raise ValidationError("Publication year cannot be in the future.")

        # Save the serializer data if validation passes
        serializer.save()


# BookUpdateView is a view that will update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# BookDeleteView is a view that will delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


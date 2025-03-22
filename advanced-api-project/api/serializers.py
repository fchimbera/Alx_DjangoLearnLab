from rest_framework import serializers
from .models import Book, Author
from datetime import date

# Create a serializer class for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    from datetime import date
from rest_framework import serializers

def validate_publication_year(self, value):
    # Get the current year
    current_year = date.today().year

    # Check if the publication year is in the future
    if value > current_year:
        raise serializers.ValidationError("Publication year cannot be in the future.")

    return value



# Create a serializer class for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'books']
        books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
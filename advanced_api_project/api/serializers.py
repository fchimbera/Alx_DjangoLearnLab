from rest_framework import serializers
from .models import Book, Author
import datetime

# Create a serializer class for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        # Get the current year
        current_year = datetime.date.today().year

        # Check if the publication_year is in the future
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        return value


# Create a serializer class for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = 'name'
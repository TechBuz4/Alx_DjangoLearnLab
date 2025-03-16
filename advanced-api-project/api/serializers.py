from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


"""
Model-Serializer Relationship Explanation
The Author model has a one-to-many relationship with the Book model using a ForeignKey.
The BookSerializer includes validation for publication_year to ensure books are not set in the future.
The AuthorSerializer uses a nested BookSerializer (books = BookSerializer(many=True, read_only=True)) to dynamically include all books related to an author.

"""

class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book model with validation for publication_year."""
    
    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model with nested books."""
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

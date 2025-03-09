from rest_framework import serializers
from .models import Book 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
         # Includes all fields from the Book model
        fields = '__all__' 

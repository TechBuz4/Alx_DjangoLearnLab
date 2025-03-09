from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all book records
    serializer_class = BookSerializer  # Use the serializer to convert data to JSON


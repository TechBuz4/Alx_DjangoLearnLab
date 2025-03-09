from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all book records
    serializer_class = BookSerializer  # Use the serializer to convert data to JSON

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations on the Book model.
    """
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer  # Use the BookSerializer for data representation
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users only

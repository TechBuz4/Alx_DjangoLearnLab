from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations on the Book model.
    """
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer  # Use the BookSerializer for data representation

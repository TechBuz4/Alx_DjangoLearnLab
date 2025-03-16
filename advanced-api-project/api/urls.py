from django.urls import path
from api.views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('api.urls')),
    path('', BookGenericAPIView.as_view(), name='book-generic-api'),
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Get a single book
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]

from django.shortcuts import render
from .models import Book
from .models import Library

# Create your views here.
def book_list_view(request):
    """View to list all books with their authors."""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.htm", {"books": books})

class LibraryDetailView(DetailView):
    """View to display a library's details and its books."""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

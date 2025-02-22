from relationship_app.models import Author, Book
# Query all books by a specific author.
def get_books_by_author(author_name):
    """Returns all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        print(f"Books by {author_name}:")
        for book in books_in_library:
            print(book.title)  
        return list(Book.objects.filter(author=author))

    except Author.DoesNotExist:
        return []

#List all books in a library.
def get_books_in_library(library_name):
    """Returns all books in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library_name}:")
        for book in books_in_library:
            print(book.title)
        return list(library.books.all())
    except Library.DoesNotExist:
        return []

    

#Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    """Returns the librarian for a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"The librarian for {library_name} is {librarian.name}")
        return librarian
    except (Library.DoesNotExist, AttributeError): 
        # AttributeError if no librarian is assigned
        return None

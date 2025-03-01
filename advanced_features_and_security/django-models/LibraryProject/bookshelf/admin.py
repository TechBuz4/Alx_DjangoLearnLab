from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display columns in admin list view
    list_filter = ('publication_year', 'author')  # Filters for better usability
    search_fields = ('title', 'author')  # Enable search functionality


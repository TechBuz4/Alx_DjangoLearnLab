from django import forms
from bookshelf.models import Book

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)


from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic
from catalog.models import Book, Author, BookInstance, Genre


class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book


def index(request):
    """View function for home page of site."""

    all_books = Book.objects.all()

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'all_books': all_books,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    print(Author.objects.all()[0].last_name)
    print(Author.objects.all()[0].first_name)
    # Render the HTML template index_catalog.html with the data in the context variable
    return render(request, 'index.html', context=context)
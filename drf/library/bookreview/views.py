from django.shortcuts import render

from rest_framework import generics

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


def index_view(request):
    response = {
        'authors': Author.objects.all(),
    }

    return render(request, 'bookreview/index.html', response)


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorInstanceView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets
from book.models import Book
from django.http import HttpResponse
from .serializers import BookSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


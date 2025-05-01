from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "description", "genre", "isbn", "publication_date", "average_rating"]
        read_only_fields = ["created_at", "updated_at"]
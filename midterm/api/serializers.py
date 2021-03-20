from rest_framework import serializers

from .models import Book, Journal


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'genre',)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class JournalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'type',)


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

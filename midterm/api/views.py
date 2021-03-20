from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Book, Journal
from .serializers import BookListSerializer, BookSerializer, JournalSerializer, JournalListSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.action == 'list' or self.action == 'get':
            return Book.objects.all()
        else:
            if self.request.user.role == 'super admin':
                return Book.objects.all()
            else:
                raise ValueError("You cannot modify the data. You have not enough privileges.")

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer


class JournalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.action == 'list' or self.action == 'get':
            return Journal.objects.all()
        else:
            if self.request.user.role == 'super admin':
                return Journal.objects.all()
            else:
                raise ValueError("You cannot modify the data. You have not enough privileges.")

    def get_serializer_class(self):
        if self.action == 'list':
            return JournalListSerializer
        return JournalSerializer

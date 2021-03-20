from django.contrib import admin
from .models import Book, Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'created_at', 'genre', 'num_pages']
    ordering = ['name', 'price']
    search_fields = ['name']
    list_filter = ['created_at', 'price', 'genre']


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'created_at', 'type', 'publisher']
    ordering = ['name', 'price']
    search_fields = ['name', 'publisher']
    list_filter = ['created_at', 'type', 'price']
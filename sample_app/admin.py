from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',) 

admin.site.register(Book, BookAdmin) 


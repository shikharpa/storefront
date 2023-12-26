from django.contrib import admin
from bookapi.models import Bookshelf, Reviews


class BookshelfAdmin(admin.ModelAdmin):
    list_display=('title', 'Author','genre','publish_year')
    list_filter=('Author','genre','publish_year')

class Reviewsadmin(admin.ModelAdmin):
    list_display=('book', 'reviews', 'userName')

admin.site.register(Bookshelf, BookshelfAdmin)
admin.site.register(Reviews, Reviewsadmin)

# Register your models here.

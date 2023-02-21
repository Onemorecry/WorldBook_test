from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, Bookinstance

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(Bookinstance)

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)


class AutorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',)
    fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


admin.site.register(Author, AutorAdmin)


class Booksinstanceinline(admin.TabularInline):
    model = Bookinstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    inlines = [Booksinstanceinline]


@admin.register(Bookinstance)
class BookinstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')})
    )

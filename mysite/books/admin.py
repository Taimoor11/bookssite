from django.contrib import admin
from .models import Publisher,Author,Books, Category, Comment, CenterContentModel, MarketingContent, ScrollAbleContent
from import_export.admin import  ImportExportModelAdmin
from .resources import BookResource


# Register your models here.

class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(ImportExportModelAdmin):
    list_display = ('title', 'slug', 'publisher', 'publication_date', 'features', 'isbn_no')
    list_editable = ("features", 'isbn_no')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_vertical = ['authors']
    prepopulated_fields = {'slug': ('title',)}





@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Books, BookAdmin)


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'book', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')



@admin.register(CenterContentModel)
class CenterContentAdmin(ImportExportModelAdmin):
    list_display = ('title', 'discription', 'call_to_action_value', 'call_to_action_value', 'html_content')
    list_filter = ('title', 'discription', 'html_content'  )

@admin.register(MarketingContent)
class MarketingContentAdmin(ImportExportModelAdmin):
    list_display = ('title', 'sequence_no' , 'html_content')

@admin.register(ScrollAbleContent)
class ScrollABleContentAdmin(ImportExportModelAdmin):
    list_display = ('title', 'html_content')



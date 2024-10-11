from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'type', 'author', 'p_rating')
    list_filter = ('type', 'author', 'p_rating')
    search_fields = ('header',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_rating')
    list_filter = ('user', 'user_rating')
    search_fields = ('user_rating',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('date_time_comment', 'c_rating')
    list_filter = ('date_time_comment', 'c_rating')
    search_fields = ('text_comment', 'c_rating')


class PostAdmin(TranslationAdmin):
    model = Post


class CategoryAdmin(TranslationAdmin):
    model = Category


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Post_Category)
admin.site.register(Comment, CommentAdmin)

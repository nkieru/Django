from .models import Post, Category
from modeltranslation.translator import register, TranslationOptions



@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('header', 'text',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
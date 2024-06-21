from django_filters import FilterSet, ModelChoiceFilter, DateFilter, ModelMultipleChoiceFilter
from .models import Post, Author, Category
from django import forms


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Все авторы',
    )

    date_time = DateFilter(
        field_name='date_time',
        lookup_expr='gte',
        label='Не раньше указанной даты:',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    categories = ModelMultipleChoiceFilter(
        field_name='categories',
        queryset=Category.objects.all(),
        label='Категория',
        conjoined=True,
    )

    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
        }


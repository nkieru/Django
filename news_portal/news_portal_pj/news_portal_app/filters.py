from django_filters import FilterSet, ModelChoiceFilter, DateFilter, ModelMultipleChoiceFilter
from .models import Post, Author, Category
from django import forms
from django.utils.translation import gettext_lazy as _

class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label=_('Author'),
        empty_label=_('All authors'),
    )

    date_time = DateFilter(
        field_name='date_time',
        lookup_expr='gte',
        label=_('Before the date:'),
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    categories = ModelMultipleChoiceFilter(
        field_name='categories',
        queryset=Category.objects.all(),
        label=_('Category'),
        conjoined=True,
    )

    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
        }

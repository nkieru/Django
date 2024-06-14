from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class NewsForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'header',
            'categories',
            'text'
        ]

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get("header")
        text = cleaned_data.get("text")

        if header == text:
            raise ValidationError(
                "Текст должен быть не идентичен названию."
            )

        return cleaned_data

    def clean_header(self):
        header = self.cleaned_data["header"]
        if header[0].islower():
            raise ValidationError(
                "Заголовок должен начинаться с заглавной буквы."
            )
        return header


class ArticleForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'header',
            'categories',
            'text'
        ]

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get("header")
        text = cleaned_data.get("text")

        if header == text:
            raise ValidationError(
                "Текст должен быть не идентичен названию."
            )

        return cleaned_data

    def clean_header(self):
        header = self.cleaned_data["header"]
        if header[0].islower():
            raise ValidationError(
                "Заголовок должен начинаться с заглавной буквы."
            )
        return header
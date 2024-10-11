from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

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
                _("The text should not be identical to the title.")
            )

        return cleaned_data

    def clean_header(self):
        header = self.cleaned_data["header"]
        if header[0].islower():
            raise ValidationError(
                _("The title should start with a capital letter.")
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
                _("The text should not be identical to the title.")
            )

        return cleaned_data

    def clean_header(self):
        header = self.cleaned_data["header"]
        if header[0].islower():
            raise ValidationError(
                _("The title should start with a capital letter.")
            )
        return header
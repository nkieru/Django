from django import template
from django.utils.translation import gettext as _
register = template.Library()

@register.filter()
def censor(value):
    words = ['word_1', 'word_2', 'word_3', 'word_4', _('word_1'), _('word_2'), _('word_3'), _('word_4'), ]

    if not isinstance(value, str):
        raise ValueError(_('The variable is not a string'))

    check_text = value.lower().split(' ')
    for word in words:
        if word in check_text:
            value = value.replace(word, word[0] + ('*' * (len(word)-1)))
    return f'{value}'
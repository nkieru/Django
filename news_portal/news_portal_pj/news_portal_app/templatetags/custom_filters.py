from django import template
register = template.Library()

@register.filter()
def censor(value):
    words = ['слово_1', 'слово_2', 'слово_3', 'слово_4', ]

    if not isinstance(value, str):
        raise ValueError('Переменная не является строкой')

    check_text = value.lower().split(' ')
    for word in words:
        if word in check_text:
            value = value.replace(word, word[0] + ('*' * (len(word)-1)))
    return f'{value}'
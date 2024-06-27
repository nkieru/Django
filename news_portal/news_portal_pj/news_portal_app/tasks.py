from datetime import datetime, timedelta
# import datetime
from .models import Post, Category
from django.conf import settings
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@shared_task
def weekly_news():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(date_time__gte=last_week)
    categories = set(posts.values_list('categories__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'weekly_news.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
        )

    msg = EmailMultiAlternatives(
        subject='Новости за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def new_post(pk):
    post = Post.objects.get(pk=pk)
    categories = post.categories.all()
    header = post.header
    subscribers_emails = []

    for c in categories:
        subscribers = c.subscribers.all()
        subscribers_emails += [i.email for i in subscribers]

    html_content = render_to_string(
        'subscribers_new_mail.html',
        {'text': post.header,
         'link': f' {settings.SITE_URL}/news/{pk}'
         }

    )

    msg = EmailMultiAlternatives(
        subject=header,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

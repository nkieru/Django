from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_save
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
from .models import Post_Category, Post
# from news_portal_pj import settings
from .tasks import new_post
#
#
#
# def send_m(preview, pk, header, subscribers):
#     html_content = render_to_string(
#         'subscribers_new_mail.html',
#         {'text': preview,
#          'link': f' {settings.SITE_URL}/news/{pk}'
#          }
#
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=header,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
# @receiver(m2m_changed, sender=Post_Category)
# def new_post_mail(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.categories.all()
#         subscribers_emails = []
#
#         for c in categories:
#             subscribers = c.subscribers.all()
#             subscribers_emails += [i.email for i in subscribers]
#
#         send_m(instance.preview(), instance.pk, instance.header, subscribers_emails)

@receiver(m2m_changed, sender=Post_Category)
def new_post_mail(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        new_post.delay(instance.pk)

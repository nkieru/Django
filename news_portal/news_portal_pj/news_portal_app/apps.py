from django.apps import AppConfig


class NewsPortalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_portal_app'

    def ready(self):
        import news_portal_app.signals

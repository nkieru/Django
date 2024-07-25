from django.core.management.base import BaseCommand, CommandError
from news_portal_app.models import Post, Category


class Command(BaseCommand):
    help = 'Delete all news in category'

    def add_arguments(self, parser):
        parser.add_argument('categories,', type=str)

    def handle(self, *args, **options):
        answer = input(f'Delete all news in {options["categories,"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Cancelled'))
            return
        try:
            category = Category.objects.get(name=options['categories,'])
            Post.objects.filter(categories=category).delete()
            self.stdout.write(self.style.SUCCESS(
                f'Succesfully deleted all news from category {category.name}'))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {options["categories"]}'))

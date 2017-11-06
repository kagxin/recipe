from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache as django_cahce

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

#    def add_arguments(self, parser):
#        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # django_cahce.set('test', 'helloworld!')
        print(django_cahce.get('test'))
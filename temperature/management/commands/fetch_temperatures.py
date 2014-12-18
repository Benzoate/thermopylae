from django.core.management.base import BaseCommand, CommandError
from temperature import views


class Command(BaseCommand):
    help = 'Fetches latest temperatures'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        num = views.update_temperatures()
        self.stdout.write('Fetched %s temperature readings' % num)

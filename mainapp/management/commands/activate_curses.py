from django.core.management.base import BaseCommand

from mainapp.models import Courses


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(Courses.all.all().update(deleted=False))

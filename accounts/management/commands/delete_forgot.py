from django.core.management.base import BaseCommand, CommandError
from accounts.models import Forgot as x
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = x.objects.all()
        for user in users:
            if (timezone.now() - user.created).total_seconds() > 120:
                user.delete()

        print("delete successfuly ...")


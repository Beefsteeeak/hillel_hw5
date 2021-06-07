from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create random users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        number_of_users = options['number_of_users']
        users = [User(username=fake.name().lower().replace(' ', ''),
                      email=fake.email(),
                      password=make_password(fake.password(length=10, special_chars=False)))
                 for i in range(number_of_users)]
        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {number_of_users} user(s)'))

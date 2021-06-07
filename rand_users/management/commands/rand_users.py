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
        # for i in range(number_of_users):
        #     User.objects.create_user(username=fake.name().lower().replace(' ', ''),
        #                              email=fake.name().lower().replace(' ', '') + '@mail.com',
        #                              password=fake.name().lower().replace(' ', ''))
        users = []
        for i in range(number_of_users):
            u = User(username=fake.name().lower().replace(' ', ''),
                     email=fake.name().lower().replace(' ', '') + '@mail.com',
                     password=fake.name().lower().replace(' ', ''))
            users.append(u)
        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {number_of_users} user(s)'))

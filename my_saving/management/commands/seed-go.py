from django.core.management.base import BaseCommand, CommandError
# from django.conf import settings
from datetime import datetime
from django.contrib.auth import get_user_model
from faker import Faker

import environ
from ...models import Account, Transaction, Currency, Category

User = get_user_model()

env = environ.Env()


class Command(BaseCommand):
    help = 'Initial filling of the DB'

    seed_users = 10

    def handle(self, *args, **options):

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.stdout.write(self.style.WARNING(f"Start: {current_time}"))

        self.init_data_currencies()
        self.stdout.write("- Init \"Currencies\" - " + self.style.SUCCESS("Ok"))

        self.init_data_categories()
        self.stdout.write("- Init \"Categories\" - " + self.style.SUCCESS("Ok"))

        if env('APP_ENV') == 'local':
            self.add_seed_superuser(self)
            self.add_seed_users(self)

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.stdout.write(self.style.SUCCESS(f"End: {current_time}"))

    @staticmethod
    def add_seed_users(self):
        users = User.objects.all()

        cnt_new_users = self.seed_users - users.count()

        fake = Faker()

        for i in range(cnt_new_users):
            User.objects.create(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password=fake.password(),
                is_staff=False,
                is_active=True,
            )

        if cnt_new_users > 0:
            self.stdout.write(f"- Init users [{cnt_new_users}] created - " + self.style.SUCCESS("Ok"))

    @staticmethod
    def add_seed_superuser(self):

        if env('TEST_SUPERUSER_LOGIN'):
            superuser = User.objects.filter(username=env('TEST_SUPERUSER_LOGIN'))
            if not superuser.exists():
                superuser_new = User.objects.create_superuser(
                    env('TEST_SUPERUSER_LOGIN'),
                    env('TEST_SUPERUSER_EMAIL'),
                    env('TEST_SUPERUSER_PASS')
                )
                superuser_new.save()
                self.stdout.write(f"- Init superuser \"{env('TEST_SUPERUSER_LOGIN')}\" - " + self.style.SUCCESS("Ok"))

    @staticmethod
    def init_data_currencies():
        data_items = (
            {
                'title': 'Сербский динар',
                'code': 'RSD',
            },
            {
                'title': 'Доллар США',
                'code': 'USD',
            },
            {
                'title': 'Евро',
                'code': 'EUR',
            },
            {
                'title': 'Рубль',
                'code': 'RUB',
            },
        )

        sort = 0
        for item in data_items:
            sort += 100
            Currency.objects.update_or_create(
                title=item['title'],
                code=item['code'],
                sort=sort,
                user=None,
                is_global=True,
            )

    @staticmethod
    def init_data_categories():

        data_items = (
            {
                'title': 'Продукты',
                'description': 'Продукты питания',
            },
            {
                'title': 'Здоровье',
                'description': 'Расходы на здоровье',
            },
            {
                'title': 'Образование',
                'description': 'Расходы на Образование',
            },
            {
                'title': 'Транспорт',
                'description': 'Расходы на транспорт',
            },
        )

        sort = 0
        for item in data_items:
            sort += 100
            Category.objects.update_or_create(
                title=item['title'],
                description=item['description'],
                sort=sort,
                user=None,
                is_global=True,
            )

from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from django.contrib.auth import get_user_model
from faker import Faker
import random

import environ
from ...models import Account, Transaction, Currency, Category

User = get_user_model()

env = environ.Env()


class Command(BaseCommand):
    help = 'Initial filling of the DB'

    seed_users = 10
    seed_accounts = 25

    def handle(self, *args, **options):

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.stdout.write(self.style.WARNING(f"Start: {current_time}"))

        self.init_data_currencies()
        self.stdout.write("- Init \"Currencies\" - " + self.style.SUCCESS("Ok"))

        self.init_data_categories()
        self.stdout.write("- Init \"Categories\" - " + self.style.SUCCESS("Ok"))

        # Seed only in local env
        if env('APP_ENV') == 'local':
            self.add_seed_superuser(self)
            self.add_seed_users(self)
            self.add_seed_accounts(self)

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.stdout.write(self.style.SUCCESS(f"End: {current_time}"))

    @staticmethod
    def add_seed_accounts(self):
        all_users = User.objects.all()
        all_accounts = Account.objects.all()

        fake = Faker()

        cnt_new_accounts = self.seed_accounts - all_accounts.count()
        for i in range(cnt_new_accounts):
            Account.objects.create(
                title=fake.company(),
                description=fake.text(max_nb_chars=250),
                user=random.choice(list(all_users)),
            )


        if cnt_new_accounts > 0:
            self.stdout.write(f"- Init accounts [{cnt_new_accounts}] created - " + self.style.SUCCESS("Ok"))


    @staticmethod
    def add_seed_users(self):
        all_users = User.objects.all()

        cnt_new_users = self.seed_users - all_users.count()

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

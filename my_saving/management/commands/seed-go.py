from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from django.contrib.auth import get_user_model
from django_seed import Seed
import environ
from ...models import Account, Transaction, Currency, Category

User = get_user_model()

env = environ.Env()
environ.Env.read_env()


class Command(BaseCommand):
    help = 'Initial filling of the DB'

    def handle(self, *args, **options):

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.stdout.write(self.style.WARNING(f"Start: {current_time}"))

        self.init_data_currencies()
        self.stdout.write("- Init \"Currencies\" - " + self.style.SUCCESS("Ok"))

        self.init_data_categories()
        self.stdout.write("- Init \"Categories\" - " + self.style.SUCCESS("Ok"))

        if env('APP_ENV') == 'local':
            self.add_test_superuser(self)

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.stdout.write(self.style.SUCCESS(f"End: {current_time}"))

    @staticmethod
    def add_test_superuser(self):

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
                user=None
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
                user=None
            )

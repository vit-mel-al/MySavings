from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from django_seed import Seed
from ...models import Account, Transaction, Currencie, Expense, Category



class Command(BaseCommand):
    
    help = 'Initial filling of the DB'

    def handle(self, *args, **options):
      
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.stdout.write(self.style.WARNING(f"Start: {current_time}"))


        self.init_data_currencies()
        self.stdout.write("- Init \"Currencies\" - " + self.style.SUCCESS("Ok"))

        self.init_data_expenses()
        self.stdout.write("- Init \"Expenses\" - " + self.style.SUCCESS("Ok"))

        self.init_data_catrgories()
        self.stdout.write("- Init \"Catrgories\" - " + self.style.SUCCESS("Ok"))
        
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.stdout.write(self.style.SUCCESS(f"End: {current_time}"))



    def init_data_currencies(self):
    
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
            sort +=100
            Currencie.objects.update_or_create(
                title=item['title'], 
                code=item['code'], 
                sort=sort,
                user=None
            )



    def init_data_expenses(self):
        
        data_items = (
            {
                'title': 'Основные расходы/доходы',
                'description': 'Повседневный быт',
            },
        )

        sort = 0
        for item in data_items:
            sort +=100
            Expense.objects.update_or_create(
                title=item['title'], 
                description=item['description'], 
                sort=sort,
                user=None
            )
        

    def init_data_catrgories(self):
        
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
            sort +=100
            Category.objects.update_or_create(
                title=item['title'], 
                description=item['description'], 
                sort=sort,
                user=None
            )
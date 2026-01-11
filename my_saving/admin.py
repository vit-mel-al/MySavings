from django.contrib import admin
from .models import Expense, Category, Account, Currencie, Transaction 


admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Account)
admin.site.register(Currencie)
admin.site.register(Transaction)

from django.contrib import admin
from .models import Category, Account, Currency, Transaction

admin.site.register(Category)
admin.site.register(Account)
admin.site.register(Currency)
admin.site.register(Transaction)

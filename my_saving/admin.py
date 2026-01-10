from django.contrib import admin
from .models import Expense
from .models import Category
from .models import Account
from .models import Currencie
from .models import Transaction

admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Account)
admin.site.register(Currencie)
admin.site.register(Transaction)

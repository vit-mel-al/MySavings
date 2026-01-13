from django.contrib import admin
from .models import Category, Account, Currency, Transaction



class MainAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_max_show_all = 1000

admin.site.register(Category, MainAdmin)
admin.site.register(Account, MainAdmin)
admin.site.register(Currency, MainAdmin)
admin.site.register(Transaction, MainAdmin)

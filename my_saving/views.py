from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Category


def dashboard(request):
    return render(request, 'my_saving/dashboard.html')


def my_savings(request):
    accounts_list = Account.objects.all()
    return render(request, 'my_saving/accounts.html', {'accounts': accounts_list})


def accounts(request):
    accounts_list = Account.objects.all()
    return render(request, 'my_saving/accounts.html', {'accounts': accounts_list})


def categories(request):
    categories_list = Category.objects.all()
    return render(request, 'my_saving/categories.html', {'categories_list': categories_list})

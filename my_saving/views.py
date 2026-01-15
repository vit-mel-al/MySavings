from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
def dashboard(request):
    return render(request, 'my_saving/dashboard.html')


def accounts(request):
    accounts_list = Account.objects.all()
    return render(request, 'my_saving/accounts.html', {'accounts': accounts_list})

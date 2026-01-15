from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
def index(request):
    accounts = Account.objects.all()
    return render(request, 'my_saving/dashboard.html', {'accounts': accounts})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account, Category




from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required


# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'my_saving/index.html')

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




def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login")


    context = {'registerform':form}

    return render(request, 'my_saving/register.html', context=context)



def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")


    context = {'loginform':form}

    return render(request, 'my_saving/my_login.html', context=context)


def user_logout(request):

    auth.logout(request)

    return redirect("home")
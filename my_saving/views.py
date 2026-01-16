from django.shortcuts import render, redirect
from .models import Account, Category
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'my_saving/index.html')


@login_required(login_url="user_login")
def dashboard(request):
    return render(request, 'my_saving/dashboard.html')


@login_required(login_url="user_login")
def my_savings(request):
    accounts_list = Account.objects.all()
    context = {'accounts': accounts_list}
    return render(request, 'my_saving/accounts.html', context=context)


@login_required(login_url="user_login")
def accounts(request):
    accounts_list = Account.objects.all()
    context = {'accounts': accounts_list}
    return render(request, 'my_saving/accounts.html', context=context)


@login_required(login_url="user_login")
def categories(request):
    categories_list = Category.objects.all()
    context = {'categories_list': categories_list}
    return render(request, 'my_saving/categories.html', context=context)


def user_register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")

    context = {'register_form': form}

    return render(request, 'my_saving/register.html', context=context)


def user_login(request):
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

    context = {'login_form': form}

    return render(request, 'my_saving/login.html', context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("home")

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('operations', views.my_savings, name='operations'),
    path('accounts', views.accounts, name='accounts'),
    path('categories', views.categories, name='categories'),
    path('user-register', views.user_register, name="user_register"),
    path('user-login', views.user_login, name="user_login"),
    path('user-logout', views.user_logout, name="user_logout"),
]
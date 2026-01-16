from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('operations/', views.my_savings, name='operations'),
    path('accounts/', views.accounts, name='accounts'),
    path('categories/', views.categories, name='categories'),
]
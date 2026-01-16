from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('savings/', views.my_savings, name='savings'),
    path('accounts/', views.accounts, name='accounts'),
    path('categories/', views.categories, name='categories'),
]
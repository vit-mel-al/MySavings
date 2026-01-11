from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


# Статьи
class Expense(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True,)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,               
        blank=True,
    )
    sort = models.IntegerField(default=1000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True,)
    deleted_at = models.DateTimeField(null=True, blank=True,)


# Категории
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True,)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,               
        blank=True,
    )
    levet = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sort = models.IntegerField(default=1000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True,)
    deleted_at = models.DateTimeField(null=True, blank=True,)


# Счета
class Account(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True,)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    sort = models.IntegerField(default=1000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True,)
    deleted_at = models.DateTimeField(null=True, blank=True,)


# Валюты
class Currencie(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    sort = models.IntegerField(default=1000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True,)
    deleted_at = models.DateTimeField(null=True, blank=True,)


# Транзакции
class Transaction(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    expense = models.ForeignKey(Expense, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    TYPES = {
        "I": "Income",
        "E": "Expense",
        "R": "Revision",
    }
    type = models.CharField(max_length = 1, choices = TYPES)
    currencie = models.ForeignKey(Currencie, null=True, on_delete=models.CASCADE,)
    amount = models.FloatField()
    description = models.CharField(max_length=255, null=True, blank=True,)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True,)
    

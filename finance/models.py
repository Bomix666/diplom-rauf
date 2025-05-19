from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    is_income = models.BooleanField(default=False, verbose_name='Доходная категория')

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=100, verbose_name='Источник')

    def __str__(self):
        return self.name

class BudgetPlan(models.Model):
    department = models.CharField(max_length=100, verbose_name='Отдел')
    project = models.CharField(max_length=100, blank=True, null=True, verbose_name='Проект')
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Плановая сумма')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    limit = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Лимит', default=0)

    def __str__(self):
        return f"{self.department} {self.year}-{self.month}: {self.amount}₽"

class Income(models.Model):
    plan = models.ForeignKey(BudgetPlan, on_delete=models.CASCADE, related_name='incomes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, limit_choices_to={'is_income': True})
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount}₽ ({self.category})"

class Expense(models.Model):
    plan = models.ForeignKey(BudgetPlan, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, limit_choices_to={'is_income': False})
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount}₽ ({self.category})"

from django import forms
from .models import BudgetPlan, Income, Expense, Category, Source

class BudgetPlanForm(forms.ModelForm):
    class Meta:
        model = BudgetPlan
        fields = ['department', 'project', 'year', 'month', 'amount', 'limit']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['plan', 'category', 'source', 'amount', 'date', 'description']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['plan', 'category', 'source', 'amount', 'date', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'is_income']

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['name']

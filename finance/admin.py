from django.contrib import admin
from .models import Category, Source, BudgetPlan, Income, Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_income')
    list_filter = ('is_income',)
    search_fields = ('name',)

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BudgetPlan)
class BudgetPlanAdmin(admin.ModelAdmin):
    list_display = ('department', 'project', 'year', 'month', 'amount', 'limit', 'created_by', 'created_at')
    list_filter = ('year', 'month', 'department')
    search_fields = ('department', 'project')
    date_hierarchy = 'created_at'

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'source', 'date', 'created_by', 'created_at')
    list_filter = ('category', 'source', 'date')
    search_fields = ('description',)
    date_hierarchy = 'date'

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'source', 'date', 'created_by', 'created_at')
    list_filter = ('category', 'source', 'date')
    search_fields = ('description',)
    date_hierarchy = 'date'

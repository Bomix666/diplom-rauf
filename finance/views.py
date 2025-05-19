from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BudgetPlan, Income, Expense, Category, Source
from .forms import BudgetPlanForm, IncomeForm, ExpenseForm
from django.db.models import Sum

@login_required
def budget_list(request):
    # Руководитель видит только свой отдел, бухгалтер и админ — все
    if hasattr(request.user, 'role') and request.user.role == 'manager':
        budgets = BudgetPlan.objects.filter(department=request.user.department)
    else:
        budgets = BudgetPlan.objects.all()
    return render(request, 'finance/budget_list.html', {'budgets': budgets})

@login_required
def budget_create(request):
    if request.method == 'POST':
        form = BudgetPlanForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.created_by = request.user
            budget.save()
            return redirect('budget_list')
    else:
        form = BudgetPlanForm()
    return render(request, 'finance/budget_form.html', {'form': form})

@login_required
def budget_detail(request, pk):
    budget = get_object_or_404(BudgetPlan, pk=pk)
    incomes = Income.objects.filter(plan=budget)
    expenses = Expense.objects.filter(plan=budget)
    income_sum = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    expense_sum = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'finance/budget_detail.html', {
        'budget': budget,
        'incomes': incomes,
        'expenses': expenses,
        'income_sum': income_sum,
        'expense_sum': expense_sum,
    })

@login_required
def income_create(request, plan_id):
    plan = get_object_or_404(BudgetPlan, pk=plan_id)
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.created_by = request.user
            income.plan = plan
            income.save()
            return redirect('budget_detail', pk=plan_id)
    else:
        form = IncomeForm(initial={'plan': plan})
    return render(request, 'finance/income_form.html', {'form': form, 'plan': plan})

@login_required
def expense_create(request, plan_id):
    plan = get_object_or_404(BudgetPlan, pk=plan_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.created_by = request.user
            expense.plan = plan
            expense.save()
            return redirect('budget_detail', pk=plan_id)
    else:
        form = ExpenseForm(initial={'plan': plan})
    return render(request, 'finance/expense_form.html', {'form': form, 'plan': plan})

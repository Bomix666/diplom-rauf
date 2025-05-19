from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report
from .forms import ReportForm
from finance.models import BudgetPlan, Income, Expense
from django.db.models import Sum
from datetime import date

@login_required
def report_list(request):
    reports = Report.objects.filter(created_by=request.user)
    return render(request, 'reports/report_list.html', {'reports': reports})

@login_required
def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.created_by = request.user
            report.save()
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

@login_required
def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    # Получаем финансы за период
    incomes = Income.objects.filter(date__range=[report.period_start, report.period_end])
    expenses = Expense.objects.filter(date__range=[report.period_start, report.period_end])
    income_sum = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    expense_sum = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'reports/report_detail.html', {
        'report': report,
        'incomes': incomes,
        'expenses': expenses,
        'income_sum': income_sum,
        'expense_sum': expense_sum,
    })

from users.models import User
from finance.models import Category, Source, BudgetPlan, Income, Expense
from datetime import date

def run():
    # Создание пользователей
    admin = User.objects.create_user(username='admin', password='adminpass', role='admin', email='admin@demo.com')
    accountant = User.objects.create_user(username='buh', password='buhpass', role='accountant', email='buh@demo.com')
    manager = User.objects.create_user(username='chief', password='chiefpass', role='manager', department='IT', email='chief@demo.com')
    # Категории и источники
    cat_income = Category.objects.create(name='Грант', is_income=True)
    cat_expense = Category.objects.create(name='Офисные расходы', is_income=False)
    source1 = Source.objects.create(name='Бюджет')
    source2 = Source.objects.create(name='Внешний фонд')
    # Бюджетный план
    plan = BudgetPlan.objects.create(department='IT', project='Автоматизация', year=2025, month=5, amount=100000, limit=90000, created_by=admin)
    # Доходы
    Income.objects.create(plan=plan, category=cat_income, source=source1, amount=70000, date=date(2025,5,1), description='Поступление гранта', created_by=accountant)
    # Расходы
    Expense.objects.create(plan=plan, category=cat_expense, source=source2, amount=30000, date=date(2025,5,10), description='Покупка техники', created_by=manager)
    print('Тестовые данные успешно добавлены.')

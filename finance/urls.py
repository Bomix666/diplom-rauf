from django.urls import path
from . import views

urlpatterns = [
    path('finance/', views.budget_list, name='budget_list'),
    path('finance/create/', views.budget_create, name='budget_create'),
    path('finance/<int:pk>/', views.budget_detail, name='budget_detail'),
    path('finance/<int:plan_id>/income/add/', views.income_create, name='income_create'),
    path('finance/<int:plan_id>/expense/add/', views.expense_create, name='expense_create'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/read/<int:pk>/', views.notification_read, name='notification_read'),
]

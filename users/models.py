from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 'admin'
    ACCOUNTANT = 'accountant'
    MANAGER = 'manager'
    ROLE_CHOICES = [
        (ADMIN, 'Администратор'),
        (ACCOUNTANT, 'Бухгалтер'),
        (MANAGER, 'Руководитель'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ACCOUNTANT)
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отдел')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

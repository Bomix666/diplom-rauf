from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'department', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'department', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'department')

from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read', 'type')
    list_filter = ('is_read', 'type', 'created_at')
    search_fields = ('message',)
    date_hierarchy = 'created_at'

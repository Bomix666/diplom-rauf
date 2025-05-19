from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'report_type', 'period_start', 'period_end', 'created_by', 'created_at')
    list_filter = ('report_type', 'period_start', 'period_end')
    search_fields = ('title',)
    date_hierarchy = 'created_at'

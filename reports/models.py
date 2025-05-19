from django.db import models
from users.models import User

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('summary', 'Сводный'),
        ('detailed', 'Детализированный'),
        ('custom', 'Пользовательский'),
    ]
    title = models.CharField(max_length=200)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    period_start = models.DateField()
    period_end = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='reports/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.get_report_type_display()})"

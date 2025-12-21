from django.contrib import admin
from .models import Unit, Assessment, PerformanceStatus, Reminder

admin.site.register(Unit)
admin.site.register(Assessment)
admin.site.register(PerformanceStatus)
admin.site.register(Reminder)

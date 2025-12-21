from django.db import models
from django.contrib.auth.models import User

class Unit(models.Model):
    unit_name = models.CharField(max_length=200)
    unit_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.unit_code} - {self.unit_name}"


class Assessment(models.Model):
    ASSESSMENT_CHOICES = (
        ('assignment', 'Assignment'),
        ('cat', 'CAT'),
        ('exam', 'Exam'),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='assessments')
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_CHOICES)
    score = models.FloatField()
    max_score = models.FloatField(default=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.student.username} - {self.unit.unit_code} - {self.assessment_type}"


class PerformanceStatus(models.Model):
    STATUS_CHOICES = (
        ('safe', 'Safe'),
        ('at_risk', 'At Risk'),
        ('failing', 'Failing'),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='performance_statuses')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='performance_statuses')
    current_average = models.FloatField(default=0.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='safe')
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.unit.unit_code} - {self.status}"


class Reminder(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    message = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    REMINDER_TYPE = (
        ('assignment', 'Assignment'),
        ('exam', 'Exam'),
        ('study', 'Study'),
    )
    type = models.CharField(max_length=20, choices=REMINDER_TYPE)

    def __str__(self):
        return f"Reminder for {self.student.username} - {self.type}"

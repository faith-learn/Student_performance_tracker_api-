from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE) 
    marks = models.IntegerField()
    grade = models.CharField(max_length=5)
    status = models.CharField(max_length=20)  # e.g. Pass, Fail, Improving
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.unit.name}"

class Reminder(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {self.student.username}"
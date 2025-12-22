from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES) # Fixed this line

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Assessment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE) 
    marks = models.IntegerField()
    grade = models.CharField(max_length=5)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.unit.name}"

class Unit(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
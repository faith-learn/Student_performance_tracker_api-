from django.test import TestCase
from django.contrib.auth.models import User
from .models import Unit, Assessment


class AssessmentTestCase(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(username="student", password="pass")
        self.unit = Unit.objects.create(name="Mathematics")

    def test_performance_status_auto_generated(self):
        assessment = Assessment.objects.create(
            student=self.student,
            unit=self.unit,
            marks=80
        )
        self.assertEqual(assessment.status, "Excellent")

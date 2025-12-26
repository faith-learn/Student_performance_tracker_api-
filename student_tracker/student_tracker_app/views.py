from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Unit, Assessment, Reminder
from .serializers import (
    UnitSerializer,
    AssessmentSerializer,
    ReminderSerializer
)

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssessmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # lecturers (staff) can see all assessments
        if user.is_staff:
            return Assessment.objects.all()

        # students see only their own assessments
        return Assessment.objects.filter(student=user)


class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Reminder.objects.all()

        return Reminder.objects.filter(student=user)

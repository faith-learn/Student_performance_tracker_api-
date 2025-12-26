from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Unit, Assessment, Reminder
from .serializers import UnitSerializer, AssessmentSerializer, ReminderSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssessmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Assessment.objects.all()
        return Assessment.objects.filter(student=user)

    def perform_create(self, serializer):
        """
        Automatically assign performance status
        """
        marks = serializer.validated_data.get("marks")

        if marks >= 50:
            status = "Pass"
        else:
            status = "Fail"

        serializer.save(student=self.request.user, status=status)


class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

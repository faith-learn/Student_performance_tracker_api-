from rest_framework import viewsets, permissions
from .models import Unit, Assessment, Reminder
from .serializers import UnitSerializer, AssessmentSerializer, ReminderSerializer
from .permissions import IsLecturer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated, IsLecturer]


class AssessmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Assessment.objects.all()
        return Assessment.objects.filter(student=user)


class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(student=self.request.user)

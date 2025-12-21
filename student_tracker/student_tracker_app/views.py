from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Added Reminder and PerformanceStatus to models
from .models import Unit, Assessment, Reminder, PerformanceStatus 

# Added ReminderSerializer and PerformanceStatusSerializer to serializers
from .serializers import (
    UnitSerializer, 
    AssessmentSerializer, 
    ReminderSerializer, 
    PerformanceStatusSerializer
)

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_user(
            username=username,
            password=password
        )

        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
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
        if user.is_staff:
            return Assessment.objects.all()
        return Assessment.objects.filter(student=user)

# --- NEW VIEWSETS ADDED BELOW ---

class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Reminder.objects.all()
        # Assuming your Reminder model has a 'user' or 'student' field
        return Reminder.objects.filter(student=user)

class PerformanceStatusViewSet(viewsets.ModelViewSet):
    queryset = PerformanceStatus.objects.all()
    serializer_class = PerformanceStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

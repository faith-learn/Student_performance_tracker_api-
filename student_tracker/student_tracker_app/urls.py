from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UnitViewSet, 
    AssessmentViewSet, 
    RegisterView,
    ReminderViewSet,
    PerformanceStatusViewSet
)

router = DefaultRouter()
router.register(r'units', UnitViewSet, basename='unit')
router.register(r'assessments', AssessmentViewSet, basename='assessment')
router.register(r'reminders', ReminderViewSet, basename='reminder')
router.register(r'performance-status', PerformanceStatusViewSet, basename='performance-status')

urlpatterns = [
    path('auth/signup/', RegisterView.as_view(), name='signup'),
    path('', include(router.urls)),
]
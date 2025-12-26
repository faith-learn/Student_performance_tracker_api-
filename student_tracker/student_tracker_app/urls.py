from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnitViewSet, AssessmentViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'units', UnitViewSet, basename='unit')
router.register(r'assessments', AssessmentViewSet, basename='assessment')
router.register(r'reminders', ReminderViewSet, basename='reminder')

urlpatterns = [
    path('', include(router.urls)),
]
 
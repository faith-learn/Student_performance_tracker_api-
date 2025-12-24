from rest_framework.routers import DefaultRouter
from .views import UnitViewSet, AssessmentViewSet, ReminderViewSet

router = DefaultRouter()
router.register('units', UnitViewSet)
router.register('assessments', AssessmentViewSet, basename='assessment')
router.register('reminders', ReminderViewSet, basename='reminder')

urlpatterns = router.urls

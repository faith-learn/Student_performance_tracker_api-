from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'units', UnitViewSet, basename='unit')
router.register(r'assessments', AssessmentViewSet, basename='assessment')

urlpatterns = [
    path('auth/signup/', RegisterView.as_view(), name='signup'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls

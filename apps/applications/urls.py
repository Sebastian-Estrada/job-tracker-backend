from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet, JobPositionViewSet, ApplicationStatusViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'job-positions', JobPositionViewSet)
router.register(r'application-statuses', ApplicationStatusViewSet)
router.register(r'job-applications', JobApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

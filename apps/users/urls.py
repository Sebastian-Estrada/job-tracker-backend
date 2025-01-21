from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, UserViewSet, UserLoginAPIView, LogoutView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')  # Prefijo vacío

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]

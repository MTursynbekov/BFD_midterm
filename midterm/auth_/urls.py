from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='auth_')
urlpatterns = [
    path('login/', obtain_jwt_token)
]

urlpatterns += router.urls
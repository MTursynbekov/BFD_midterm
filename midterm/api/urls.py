from rest_framework.routers import DefaultRouter

from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='api')
router.register(r'journals', BookViewSet, basename='api')

urlpatterns = router.urls

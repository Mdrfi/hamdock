from rest_framework.routers import DefaultRouter
from app.api.app_viewset import AppViewSet
router = DefaultRouter()

router.register(r'apps', AppViewSet, basename='apps')

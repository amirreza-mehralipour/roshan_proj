from django.urls import path, include
from .views import DatasetViewSet, TagViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'dataset', DatasetViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
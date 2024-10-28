from django.urls import path, include
from .views import LlistCreateDataset, DatasetViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'dataset', DatasetViewSet)

urlpatterns = [
    # path('dataset/', LlistCreateDataset.as_view()),
    path('', include(router.urls)),
]
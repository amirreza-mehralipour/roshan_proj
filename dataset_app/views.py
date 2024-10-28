from .models import Dataset, Tag
from .serializers import DatasetSerializer, TagSerializer
from rest_framework.viewsets import ModelViewSet


class DatasetViewSet(ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
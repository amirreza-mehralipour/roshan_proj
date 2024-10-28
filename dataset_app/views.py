from .models import Dataset, Tag
from .serializers import DatasetSerializer, TagSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class LlistCreateDataset(ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

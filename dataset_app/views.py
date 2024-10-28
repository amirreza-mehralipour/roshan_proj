from .models import Dataset, Tag
from .serializers import DatasetSerializer, TagSerializer
from rest_framework.viewsets import ModelViewSet

# I decided to use viewsets instead of APIView in the following views because it's simpler and more maintainable for this situation.
class DatasetViewSet(ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
from rest_framework.serializers import ModelSerializer
from .models import *

class DatasetSerializer(ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
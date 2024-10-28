from django.contrib.admin import register, ModelAdmin
from .models import Dataset, Tag


@register(Dataset)
class DatasetAdmin(ModelAdmin):
    pass


@register(Tag)
class TagAdmin(ModelAdmin):
    pass
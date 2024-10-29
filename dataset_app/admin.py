from django.contrib.admin import register, ModelAdmin
from .models import Dataset, Tag, Data, DataTag, AnsweredDataset


@register(Dataset)
class DatasetAdmin(ModelAdmin):
    pass


@register(Tag)
class TagAdmin(ModelAdmin):
    pass

@register(DataTag)
class DataTagAdmin(ModelAdmin):
    pass


@register(Data)
class DataAdmin(ModelAdmin):
    pass


@register(AnsweredDataset)
class AnsweredDatasetAdmin(ModelAdmin):
    pass
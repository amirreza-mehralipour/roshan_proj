from django.contrib.admin import register, ModelAdmin
from .models import *


@register(Dataset)
class DatasetAdmin(ModelAdmin):
    pass


@register(Tag)
class TagAdmin(ModelAdmin):
    pass
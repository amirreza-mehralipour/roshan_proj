from django.urls import path
from .views import LlistCreateDataset


urlpatterns = [
    path('', LlistCreateDataset.as_view())
]
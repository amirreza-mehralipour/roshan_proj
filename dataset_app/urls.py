from django.urls import path
from .views import LlistCreateDataset


urlpatterns = [
    path('dataset/', LlistCreateDataset.as_view())
]
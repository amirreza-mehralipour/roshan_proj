from django.db import models


class Dataset(models.Model):
    command = models.TextField()
    statment = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    last_updated = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(default= True)

class Tags(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete= models.CASCADE)
    description = models.CharField(max_length=255)
    state = models.BooleanField()
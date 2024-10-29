from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.description

class Dataset(models.Model):
    command = models.TextField()
    statement = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    last_updated = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return f'{self.command} | {self.statment}'
    

class DatasetTag(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete= models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    tag_status = models.BooleanField()
    operator = models.ForeignKey(User,on_delete=models.PROTECT)
    tagged_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(default= True)

    def __str__(self) -> str:
        return f'tag: {self.tag.description} dataset: {self.dataset.statment}'
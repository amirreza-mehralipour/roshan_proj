from django.db import models


class Tag(models.Model):
    description = models.CharField(max_length=255)
    state = models.BooleanField()

    def __str__(self) -> str:
        return self.description

class Dataset(models.Model):
    command = models.TextField()
    statment = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    last_updated = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(default= True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f'{self.command} | {self.statment}'
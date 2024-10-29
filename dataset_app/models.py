from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    last_updated_at = models.DateTimeField(auto_now= True)
    

    def __str__(self) -> str:
        return self.description

class Data(models.Model):
    description = models.TextField()
    statement = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    last_updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return f'{self.description} | {self.statement}'
    

class DataTag(models.Model):
    data = models.ForeignKey(Data, on_delete= models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add= True)
    last_updated_at = models.DateTimeField(auto_now= True)



    def __str__(self) -> str:
        return f'data: {self.data.statement} | tag: {self.tag.description}'
    

class AnsweredDataTag(models.Model):
    datatag = models.ForeignKey(DataTag, on_delete= models.PROTECT)
    operator = models.ForeignKey(User, on_delete= models.PROTECT, null= True, default= None)
    created_at = models.DateTimeField(auto_now_add= True)
    tag_status = models.BooleanField(null= True, default= None)
    tagged_at = models.DateTimeField(blank= True, null= True)
    last_changed_tag_at = models.DateTimeField(auto_now= True)
    
    def save(self, *args, **kwargs) -> None:
        if self.operator != None and self.tagged_at == None:
            self.tagged_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'tagged by {self.operator} on {self.datatag} with status: {self.tag_status}'


class Dataset(models.Model):
    answered_datatags = models.ManyToManyField(AnsweredDataTag)
    is_active = models.BooleanField(default= True)

    # def __str__(self) -> str:
    #     data = self.DataTag.all()
    #     return f'{data[0]}'
    

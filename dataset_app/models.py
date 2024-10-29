from django.db import models
# from django.contrib.auth.models import User


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
        return f'tag: {self.tag.description} dataset: {self.data.statement}'
    

class AnsweredDataTag(models.Model):
    datatag = models.ForeignKey(DataTag, on_delete= models.PROTECT)
    # operator = models.ForeignKey(User, on_delete= models.PROTECT)
    tag_status = models.BooleanField()
    tagged_at = models.DateTimeField(auto_now_add= True)
    last_changed_tag_at = models.DateTimeField(auto_now= True)

    # def __str__(self) -> str:
    #     return super().__str__()


class Dataset(models.Model):
    answered_datatags = models.ManyToManyField(AnsweredDataTag)
    is_active = models.BooleanField(default= True)

    # def __str__(self) -> str:
    #     data = self.DataTag.all()
    #     return f'{data[0]}'
    


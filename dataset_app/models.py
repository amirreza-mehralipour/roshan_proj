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
    tag_status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add= True)
    last_updated_at = models.DateTimeField(auto_now= True)



    def __str__(self) -> str:
        return f'tag: {self.tag.description} dataset: {self.data.statement}'
    

class Dataset(models.Model):
    datatag = models.ManyToManyField(DataTag)
    is_active = models.BooleanField(default= True)

    # def __str__(self) -> str:
    #     data = self.DataTag.all()
    #     return f'{data[0]}'
    

class AnsweredDataset(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete= models.PROTECT)
    # operator = models.ForeignKey(User, on_delete= models.PROTECT)
    tagged_at = models.DateTimeField(auto_now_add= True)
    last_changes_in_tags = models.DateTimeField(auto_now= True)

    # def __str__(self) -> str:
    #     return super().__str__()


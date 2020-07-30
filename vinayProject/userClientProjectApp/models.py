from django.db import models


# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    def __str__(s):
        return s.name
    class Meta:
        db_table = 'User'

class Client(models.Model):
    client_name=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(s):
        return s.client_name
    class Meta:
        db_table = 'Client'

class Project(models.Model):
    project_name=models.CharField(max_length=30)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    users = models.ManyToManyField(User,blank=True)  #Many To Many Field used because a project can be assigned to multiple user
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Project'

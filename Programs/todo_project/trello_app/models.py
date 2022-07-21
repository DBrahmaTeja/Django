from django.db import models
from django.utils import timezone
# Create your models here.

#ORM: object relational mapper

#inherit from the Model class provided by Django
#inheritance: to reuse the code
#model is base class
#task is child class

#class => table in DB
#fields -> columns in the table(fields are part of django model class)
class TaskList(models.Model):
    name=models.CharField(max_length=50)
    created_at = models.DateTimeField(
    default=timezone.now()
    )
    def __str__(self):##to_string()
        return f"{self.name}---{self.created_at}"

class Task(models.Model):
    # maps to VARCHAR
    name=models.CharField(max_length=50)
    desc=models.TextField()
    created_at=models.DateTimeField(
        default=timezone.now()
    )
    due_date=models.DateTimeField()
    list=models.ForeignKey(TaskList,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}---{self.desc}"





        

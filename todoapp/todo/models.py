from django.db import models


# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    info = models.CharField(max_length=50, default='')
   

class ArchivedItem(models.Model):
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    info = models.CharField(max_length=50, default='' )
   

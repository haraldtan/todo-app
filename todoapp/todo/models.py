from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()

class ArchivedItem(models.Model):
    content = models.TextField()
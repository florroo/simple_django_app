from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length = 75)
    category = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length = 75)
    category = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(blank = True)
    banner = models.ImageField(default='default.png', blank = True)

    def __str__(self):
        return self.title
        
    
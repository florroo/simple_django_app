from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "documents")
    title = models.CharField(max_length = 75)
    description = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(blank = True)
    file = models.FileField(blank = True, null = True)

    class Meta:
        unique_together = ("owner", "slug")

    def __str__(self):
        return self.title
        
    
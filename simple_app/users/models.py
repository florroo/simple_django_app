from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length = 75)
    lastname = models.CharField(max_length = 75)
    password = models.CharField(max_length = 50)
    email = models.TextField(blank = True)

    def __str__(self):
        return self.email
        
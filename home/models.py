from django.db import models

# Create your models here.

class contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name
    
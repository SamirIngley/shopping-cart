from django.db import models
from __future__ import unicode_literals
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()

    def __str__(self):
        return self.name
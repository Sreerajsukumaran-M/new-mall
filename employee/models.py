from django.db import models
from store.models import Store

class Employee(models.Model):
    name = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
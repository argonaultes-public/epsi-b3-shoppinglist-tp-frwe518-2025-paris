from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_serial = models.IntegerField()

    def __str__(self):
        return self.item_name

class Store(models.Model):
    store_name = models.CharField(max_length=100)

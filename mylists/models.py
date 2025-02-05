from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_serial = models.IntegerField()
    store = models.ForeignKey('Store', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.item_name

class Store(models.Model):
    store_name = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name

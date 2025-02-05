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


class ShopList(models.Model):
    shoplist_name = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default='Green')
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.shoplist_name
from django.contrib import admin
from .models import Store, Item, ShopList
# Register your models here.

admin.site.register([Store, Item, ShopList])
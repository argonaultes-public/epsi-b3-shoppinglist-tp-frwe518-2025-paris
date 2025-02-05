from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store, Item, ShopList

# Create your views here.

def index_view(request):
    return HttpResponse('Index of list')

def index_view_other(request):
    return HttpResponse('Index 2')

def index_view_tpl(request):
    return render(request=request, template_name='tpl.html')

def index_view_tpl_title(request):
    return render(request=request, template_name='tplcontext.html', context={'title': 'Template Context'})

def stores(request):
    stores = Store.objects.all()
    return render(request=request, template_name='stores.html', context={ 'stores': stores})

def store_details(request, store_id = 0):
    store = Store.objects.get(pk=store_id)
    items_in_store = store.item_set.all()
    return render(request=request, template_name='store.html', context={'store': store, 'items_in_store': items_in_store})

def items(request):
    items = Item.objects.all()
    return render(request=request, template_name='items.html', context={'items': items})

def item_details(request, item_id = 0):
    item = Item.objects.get(pk=item_id)
    return render(request=request, template_name='item.html', context={'item': item})

def shop_lists(request):
    shop_lists = ShopList.objects.prefetch_related('items')
    return render(request=request, template_name='shoplists.html', context={'shop_lists': shop_lists})

def display_form_shop_list(request):
    return render(request=request, template_name='new_shoplist.html', context={})

def new_shop_list(request):
    shoplist_name = request.POST['shoplist_name']
    ShopList.objects.create(shoplist_name=shoplist_name)
    return redirect("list_of_shoplists")
from django.shortcuts import render
from django.http import HttpResponse
from .models import Store, Item

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

def items(request):
    items = Item.objects.all()
    return render(request=request, template_name='items.html', context={'items': items})

def item_details(request, item_id = 0):
    item = Item.objects.get(pk=item_id)
    return render(request=request, template_name='item.html', context={'item': item})
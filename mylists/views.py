from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    return HttpResponse('Index of list')

def index_view_other(request):
    return HttpResponse('Index 2')
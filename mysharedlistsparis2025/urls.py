"""
URL configuration for mysharedlistsparis2025 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from mylists import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index_view),
    path("index_view_other/", views.index_view_other),
    path("index_tpl/", views.index_view_tpl),
    path("index_tpl_2/", TemplateView.as_view(template_name='tpl.html')),
    path("index_tpl_ctx/", views.index_view_tpl_title),
    path("stores/", views.stores),
    path("stores/<int:store_id>/", views.store_details),
    path("items/", views.items),
    path("items/<int:item_id>/", views.item_details),
    path("shoplists/", views.shop_lists, name="list_of_shoplists"),
    path("shoplist/", views.display_form_shop_list),
    path("shoplist/<int:shop_list_id>/", views.shop_list_details),
    path("shoplist/new/", views.new_shop_list, name="shoplist_new"),
    path("shoplist_class/", login_required(views.ShopListView.as_view(), login_url='login_class'), name="shoplist_class"),
    path("login/", views.MyLoginView.as_view(), name='login_class'),
]

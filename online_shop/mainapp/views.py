from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import *
from .utils import *


class AllProducts(BaseMixin, ListView):
    template_name = 'mainapp/all_products.html'
    queryset = Goods.objects.all()
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context


class ShowProduct(BaseMixin, DetailView):
    template_name = 'mainapp/show_product.html'
    context_object_name = 'product'
    queryset = Goods.objects.all()

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context


class SubcategoriesByCategories(BaseMixin, ListView):
    template_name = 'mainapp/subcategories.html'
    context_object_name = 'subcategory'

    def get_context_data(self, **kwargs):
        super_context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        category = f'{self.request.path}'.split('/')[-1]
        return Subcategory.objects.filter(category__slug=category)


class GoodsBySubcategory(BaseMixin, ListView):
    template_name = 'mainapp/goods_by_subcategory.html'
    context_object_name = 'goods'

    def get_context_data(self, **kwargs):
        super_context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        subcategory = f'{self.request.path}'.split('/')[-1]
        return Goods.objects.filter(subcategory__slug=subcategory)

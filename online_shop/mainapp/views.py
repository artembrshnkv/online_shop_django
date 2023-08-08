from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def home_page(request):
    return render(request, template_name='mainapp/home_page.html')


class AllProducts(ListView):
    template_name = 'mainapp/all_products.html'
    queryset = Goods.objects.all()
    context_object_name = 'products'


class ShowProduct(DetailView):
    template_name = 'show_product.html'
    context_object_name = 'product'

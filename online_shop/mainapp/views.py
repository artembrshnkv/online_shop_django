from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django import http
from django.db.models import Q

from .models import *
from .utils import *
from .forms import *


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
        if Category.objects.filter(slug=category).count() != 0:
            return Subcategory.objects.filter(category__slug=category)
        else:
            raise http.Http404


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
        if Subcategory.objects.filter(slug=subcategory).count() != 0:
            return Goods.objects.filter(subcategory__slug=subcategory)
        else:
            raise http.Http404


class UserRegistration(BaseMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'mainapp/registration.html'

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context


class UserLogin(BaseMixin, LoginView):
    template_name = 'mainapp/user_login.html'

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context


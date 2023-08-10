from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django import http
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
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

    def get_data(self):
        product_id = f'{self.request.path}'.split('/')[-1]
        user_id = self.request.user.pk
        data = {
            'product_id': product_id,
            'user_id': user_id
        }
        return data

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        context['product_id'] = self.get_data()['product_id']
        context['user_id'] = self.get_data()['user_id']
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


class UserAccount(BaseMixin, TemplateView):
    template_name = 'mainapp/user_account.html'

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context


class MyCart(BaseMixin, ListView):
    template_name = 'mainapp/my_cart.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        product_slug = f'{Cart.objects.filter(user_id=self.request.user.pk)[0]}'.split('_')[1]
        return Goods.objects.filter(slug=product_slug)


def user_logout(request):
    logout(request)
    return redirect('all_products')

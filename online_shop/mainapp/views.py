from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView
from django import http
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *
from .forms import *


class AllProducts(BaseMixin, ListView):
    template_name = 'mainapp/all_products.html'
    queryset = Goods.objects.all()
    context_object_name = 'products'
    paginate_by = 1


    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        if self.request.GET.get('min_price'):
            return Goods.objects.all().order_by('price').prefect_releted('category')
        elif self.request.GET.get('max_price'):
            return Goods.objects.all().order_by('-price').prefetch_related('category')
        else:
            return Goods.objects.all().select_related('category')


class ShowProduct(BaseMixin, DetailView):
    template_name = 'mainapp/show_product.html'
    context_object_name = 'product'
    queryset = Goods.objects.all().select_related('category')

    def get_data(self):
        product_id = f'{self.request.path}'.split('/')[-1]
        user_id = self.request.user.pk
        category = Goods.objects.get(id=product_id).category
        subcategory = Goods.objects.get(id=product_id).subcategory
        if self.request.GET.get('bad_at_first'):
            comments = Comment.objects.filter(product_id=product_id).order_by('rating')
        elif self.request.GET.get('good_at_first'):
            comments = Comment.objects.filter(product_id=product_id).order_by('-rating')
        else:
            comments = Comment.objects.filter(product_id=product_id).select_related('username')

        avg_rating = comments.aggregate(Avg('rating'))
        data = {
            'category': category,
            'subcategory': subcategory,
            'product_id': product_id,
            'user_id': user_id,
            'comments': comments,
            'avg_rating': avg_rating
        }
        return data

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        self_data = self.get_data()
        context = dict(list(super_data.items()) + list(c_def.items()) + list(self_data.items()))
        context['comments_sort_menu'] = comments_sort_menu
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
            return Subcategory.objects.filter(category__slug=category).select_related('category')
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
    success_url = reverse_lazy('user_login')

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


class UserAccount(LoginRequiredMixin, BaseMixin, TemplateView):
    template_name = 'mainapp/user_account.html'

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context


class MyCart(LoginRequiredMixin, BaseMixin, ListView):
    template_name = 'mainapp/my_cart.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        context = dict(list(super_data.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        try:
            products_slugs = [str(n).split('_')[1] for n in Cart.objects.filter(user_id=self.request.user.pk)]
            return Goods.objects.filter(slug__in=products_slugs)
        except IndexError:
            pass


class AddComment(LoginRequiredMixin, BaseMixin, CreateView):
    form_class = AddCommentForm
    template_name = 'mainapp/add_comment.html'
    success_url = reverse_lazy('all_products')

    def get_data(self):
        product_id = f'{self.request.path}'.split('/')[-2]
        user_id = self.request.user.pk
        category = Goods.objects.get(id=product_id).category
        subcategory = Goods.objects.get(id=product_id).subcategory
        data = {
            'product_id': product_id,
            'user_id': user_id,
            'category': category,
            'subcategory': subcategory
        }
        return data

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs)
        c_def = self.get_user_context(**kwargs)
        self_data = self.get_data()
        context = dict(list(super_data.items()) + list(c_def.items()) + list(self_data.items()))
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['username'] = self.get_data()['user_id']
        kwargs['initial']['product'] = self.get_data()['product_id']
        return kwargs

    def get_success_url(self):
        return reverse('show_product', kwargs={'category': self.get_data()['category'],
                                               'subcategory': self.get_data()['subcategory'],
                                               'pk': self.get_data()['product_id']})


class CommentUpdate(LoginRequiredMixin, BaseMixin, UpdateView):
    template_name = 'mainapp/comment_update.html'
    form_class = AddCommentForm
    success_url = reverse_lazy('all_products')
    # model = Comment

    def get_data(self):
        product_id = f'{self.request.path}'.split('/')[-2]
        user_id = self.request.user.pk
        category = Goods.objects.get(id=product_id).category
        subcategory = Goods.objects.get(id=product_id).subcategory
        data = {
            'product_id': product_id,
            'user_id': user_id,
            'category': category,
            'subcategory': subcategory
        }
        return data

    def get_context_data(self, **kwargs):
        super_data = super().get_context_data(**kwargs).items()
        c_def = self.get_user_context(**kwargs).items()
        context = dict(list(super_data) + list(c_def))
        return context

    def get_success_url(self):
        return reverse('show_product', kwargs={'category': self.get_data()['category'],
                                               'subcategory': self.get_data()['subcategory'],
                                               'pk': self.get_data()['product_id']})

    def get_queryset(self):
        print(Comment.objects.filter(username_id=self.get_data()['user_id'],
                                     product_id=self.get_data()['product_id']))
        return Comment.objects.filter(username_id=self.get_data()['user_id'],
                                      product_id=self.get_data()['product_id'])


def user_logout(request):
    logout(request)
    return redirect('all_products')

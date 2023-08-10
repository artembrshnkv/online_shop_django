from .models import *

menu = [
    {'name': 'Главная страница', 'url': 'all_products', 'type': 'link_button'},
    {'name': 'Категории', 'type': 'menu_dropdown'},
    {'name': 'Регистрация', 'url': 'registration', 'type': 'auth_false'},
    {'name': 'Войти', 'url': 'user_login', 'type': 'auth_false'},
    {'name': 'Аккаунт', 'url': 'user_account', 'type': 'auth_true'},
    {'name': 'Корзина', 'url': 'my_cart', 'type': 'auth_true'}
]

subcategories = Subcategory.objects.all()
categories = Category.objects.all()


class BaseMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['categories'] = categories
        context['subcategories'] = subcategories
        return context

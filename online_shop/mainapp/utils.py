from .models import *

menu = [
    {'name': 'Главная страница', 'url': 'all_products', 'type': 'link_button'},
    {'name': 'Категории', 'type': 'menu_dropdown'},
    {'name': 'Регистрация', 'url': 'registration', 'type': 'auth_false'},
    {'name': 'Войти', 'url': 'user_login', 'type': 'auth_false'},
    {'name': 'Аккаунт', 'url': 'user_account', 'type': 'auth_true'},
    {'name': 'Корзина', 'url': 'my_cart', 'type': 'auth_true'}
]

sort_menu = [
    {'title': 'По вазрастани цены', 'url': '?min_price=True'},
    {'title': 'По убыванию цены ', 'url': '?max_price=True'},

]

comments_sort_menu = [
    {'title': 'Сначало хорошие', 'url': '?good_at_first=True'},
    {'title': 'Сначало плохие', 'url': '?bad_at_first=True'}
]

subcategories = Subcategory.objects.all().select_related('category')
categories = Category.objects.all()


class BaseMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['categories'] = categories
        context['subcategories'] = subcategories
        context['sort_menu'] = sort_menu
        return context


from .models import *

menu = [
    {'name': 'Главная страница', 'url': 'all_products', 'type': 'link_button'},
    {'name': 'Категории', 'type': 'menu_dropdown'}
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

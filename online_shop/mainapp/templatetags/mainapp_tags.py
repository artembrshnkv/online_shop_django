from django import template
from mainapp.models import Cart

register = template.Library()


@register.simple_tag(name='insert_into_cart')
def insert_into_cart(product_id, user_id):
    Cart.objects.create(product_id=product_id, user_id=user_id)


@register.simple_tag()
def already_in_cart(product_id, user_id):
    return True if Cart.objects.filter(product_id=product_id, user_id=user_id).count() != 0 else False


@register.simple_tag(name='delete_from_cart')
def delete_from_cart(product_id, user_id):
    Cart.objects.filter(product_id=product_id, user_id=user_id).delete()

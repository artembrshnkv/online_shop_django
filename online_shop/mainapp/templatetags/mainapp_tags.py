from django import template
from mainapp.models import Cart

register = template.Library()


@register.simple_tag()
def insert_into_cart(product_id, user_id):
    Cart.objects.create(product_id=product_id, user_id=user_id)


@register.simple_tag()
def already_in_cart(product_id, user_id):
    return True if Cart.objects.get(product_id=product_id, user_id=user_id).count() != 0 else False
    # if Cart.objects.get(product_id=product_id, user_id=user_id).count() != 0:
    #     return True
    # else:
    #     return False


@register.simple_tag()
def delete_from_cart(product_id, user_id):
    Cart.objects.filter(product_id=product_id, user_id=user_id).delete()

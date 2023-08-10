from django import template
from mainapp.models import Cart

register = template.Library()


@register.simple_tag()
def insert_into_cart(product_id, user_id):
    Cart.objects.create(product_id=product_id, user_id=user_id)



from django import template
from mainapp.models import Cart, Comment

register = template.Library()


@register.simple_tag()
def insert_into_cart(product_id, user_id):
    Cart.objects.create(product_id=product_id, user_id=user_id)


@register.simple_tag()
def already_in_cart(product_id, user_id):
    return True if Cart.objects.filter(product_id=product_id, user_id=user_id).count() != 0 else False


@register.simple_tag()
def delete_from_cart(product_id, user_id):
    Cart.objects.filter(product_id=product_id, user_id=user_id).delete()


@register.simple_tag()
def has_comments(product_id):
    return True if Comment.objects.filter(product_id=product_id).count() != 0 else False

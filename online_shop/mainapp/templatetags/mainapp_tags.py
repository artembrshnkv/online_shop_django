from django import template
from django.contrib.auth.models import User

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


@register.simple_tag()
def get_username_by_id(user_id):
    return User.objects.get(pk=user_id).username


@register.simple_tag()
def comment_is_edited(user_id, product_id):
    time_creation = Comment.objects.get(username_id=user_id, product_id=product_id).time_creation
    time_update = Comment.objects.get(username_id=user_id, product_id=product_id).time_update
    return True if time_creation == time_update else False


@register.simple_tag()
def comment_exists(user_id, product_id):
    return True if Comment.objects.filter(username_id=user_id, product_id=product_id).count() != 0 else False

from django.urls import path
from .views import *

urlpatterns = [
    path('', AllProducts.as_view(), name='all_products'),
    path('<slug:category>/<slug:subcategory>/<int:pk>', ShowProduct.as_view(), name='show_product'),
    path('<slug:category>/<slug:subcategory>/<int:pk>/add_comment', AddComment.as_view(), name='add_comment'),
    path('<slug:category>/<slug:subcategory>/<int:pk>/update_comment', CommentUpdate.as_view(), name='update_comment'),
    path('registration', UserRegistration.as_view(), name='registration'),
    path('login', UserLogin.as_view(), name='user_login'),
    path('account', UserAccount.as_view(), name='user_account'),
    path('logout', user_logout, name='user_logout'),
    path('cart', MyCart.as_view(), name='my_cart'),
    path('<slug:slug>', SubcategoriesByCategories.as_view(), name='all_subcategories'),
    path('<slug:category>/<slug:slug>', GoodsBySubcategory.as_view(), name='goods_by_subcategory'),
]

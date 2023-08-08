from django.urls import path
from .views import *

urlpatterns = [
    path('', AllProducts.as_view()),
    path('<slug:category>/<slug:subcategory>/<int:product_id>', ShowProduct.as_view(), name='show_product')
]

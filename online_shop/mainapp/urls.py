from django.urls import path
from .views import *

urlpatterns = [
    path('', AllProducts.as_view(), name='all_products'),
    path('<slug:category>/<slug:subcategory>/<int:pk>', ShowProduct.as_view(), name='show_product'),
    path('reg', UserRegistration.as_view(), name='reg'),
    path('login', UserLogin.as_view(), name='user_login'),
    path('<slug:slug>', SubcategoriesByCategories.as_view(), name='all_subcategories'),
    path('<slug:category>/<slug:slug>', GoodsBySubcategory.as_view(), name='goods_by_subcategory'),

]

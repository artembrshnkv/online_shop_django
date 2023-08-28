from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework import routers

from .api_views import *

products_router = routers.SimpleRouter()
products_router.register('products', GoodsViewSet)

urlpatterns = [
    path('', include(products_router.urls)),
    path('', include('djoser.urls.authtoken')),
]

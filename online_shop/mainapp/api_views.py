from rest_framework import viewsets

from .models import Goods
from .serializers import GoodsApiSerializer
from .utils import ProductsPagination


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsApiSerializer
    pagination_class = ProductsPagination

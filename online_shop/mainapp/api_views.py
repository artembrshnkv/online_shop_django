from rest_framework import viewsets

from .models import Goods
from .serializers import GoodsApiSerializer


# class GoodsApiView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsApiSerializer


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsApiSerializer

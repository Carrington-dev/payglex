from rest_framework.viewsets import ModelViewSet
from forex.mixins import AllCurrencyViewMixin
from forex.models import Currency
from forex.serials import CurrencySerializer
from rest_framework.permissions import  IsAuthenticated

class CurrencyViewSet(AllCurrencyViewMixin):
    serializer_class = CurrencySerializer
    model = Currency
    queryset = Currency.objects.all()
    # permission_classes = [ IsAuthenticated ]
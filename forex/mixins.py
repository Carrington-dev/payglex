from rest_framework import  mixins, viewsets

class AllCurrencyViewMixin(mixins.ListModelMixin, \
        mixins.RetrieveModelMixin, \
        viewsets.GenericViewSet):
    pass
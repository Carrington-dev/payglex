from rest_framework import serializers
from forex.models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    rate = serializers.DecimalField(decimal_places=2, max_digits=8)
    # USD	 = serializers.DecimalField(decimal_places=2, max_digits=8)
    # EUR  = serializers.DecimalField(decimal_places=2, max_digits=8)
    # JPY	 = serializers.DecimalField(decimal_places=2, max_digits=8)
    # GBP  = serializers.DecimalField(decimal_places=2, max_digits=8)
    # CNY  = serializers.DecimalField(decimal_places=2, max_digits=8)
    # AUD  = serializers.DecimalField(decimal_places=2, max_digits=8)
    # CAD  = serializers.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        fields = ['name', 'base', 'rate',   "USD",	"EUR","JPY","GBP", "CNY", "AUD", "CAD", 'last_updated',]
        model = Currency

    

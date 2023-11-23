import decimal
from django.db import models
from django.shortcuts import get_object_or_404

class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)
    base = models.CharField(max_length=50, default='USD')
    rate = models.DecimalField(decimal_places=2, max_digits=8)

    date_created			= models.DateTimeField(verbose_name='date created', auto_now_add=True)
    last_updated			= models.DateTimeField(verbose_name='last update', auto_now=True)
    
    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        ordering = ['name']

    def __str__(self):
        return f"@  {self.name} {self.rate} / 1{self.base}"
    
    
    

    def USD(self):
        return self.rate
        
    def EUR(self):
        try:
            a = get_object_or_404(Currency, name="EUR")
            r = 1 / a.rate * self.rate
            return decimal.Decimal("{:.2f}".format(r))
        except:
            pass
        return 1
        
    def JPY(self):
        try:
            a = get_object_or_404(Currency, name="JPY")
            r =  a.rate * 1 / self.rate
            return decimal.Decimal("{:.2f}".format(r))
        except:
            pass
        return 78.98
        
    def GBP(self):
        try:
            a = get_object_or_404(Currency, name="GBP")
            r = 1 / a.rate * self.rate
            return decimal.Decimal("{:.2f}".format(r))
        except:
            pass
        return 78.98
        
    def CNY(self):
        try:
            a = get_object_or_404(Currency, name="CNY")
            r = 1 / a.rate * self.rate
            return decimal.Decimal("{:.2f}".format(r))
        except:
            pass
        return 78.98
        
    def AUD(self):
        try:
            a = get_object_or_404(Currency, name="AUD")
            r = 1 / a.rate * self.rate
            return decimal.Decimal("{:.2f}".format(r))
        except:
            pass
        return 78.98
        
    def CAD(self):
        try:
            a = get_object_or_404(Currency, name="CAD")
            r = 1 / a.rate * self.rate
            return decimal.Decimal("{:.2f}".format(r))
        except:
            pass
        return 78.98

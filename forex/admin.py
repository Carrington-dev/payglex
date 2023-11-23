from django.contrib import admin
from forex.models import Currency

@admin.register(Currency)
class CashAdmin(admin.ModelAdmin):
    '''Admin View for Cash'''

    list_display = ('name', 'base', 'rate', 'last_updated', 'date_created')
    list_filter = ('base',)
    # readonly_fields = ('',)
    search_fields = ('name',)
    date_hierarchy = 'last_updated'
    ordering = ('name',)
    list_per_page = 30
from django.urls import path, include
from rest_framework import routers
from forex import views


router = routers.DefaultRouter()

router.register('currencies', views.CurrencyViewSet, basename='currency')

urlpatterns = [
    path('', include(router.urls)),
]
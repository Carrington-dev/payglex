from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Payglen Currency Exchange Rates",
      default_version='v1',
      description="Payglen Currency Exchange Rates with 170 different currencies",
      terms_of_service="https://www.payglen.com/policies/terms/",
      contact=openapi.Contact(email="currency@payglen.com"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

  
admin.site.site_header = 'Payglen'                    # default: "Django Administration"
admin.site.index_title = 'Payglen Portal'                 # default: "Site administration"
admin.site.site_title = 'Payglen Administration'

urlpatterns = [
      path('grappelli/', include('grappelli.urls')), # grappelli URLS
      # path('admin/', admin.site.urls),
      # path('accounts/', include('myauth.urls')),

      path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
      path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

      path('', include('djoser.urls.jwt')),
      path('', include('djoser.urls')),
      path('', include('djoser.urls.authtoken')),
      path('forex/', include('forex.urls')),
]

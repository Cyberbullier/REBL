from django.urls import path, include
from shopapi.views import ApparelproductsViewSet, CategoryViewSet, \
    ShoppingcartitemViewSet, ShoppingcartViewSet

from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register(r'products', ApparelproductsViewSet, basename='product')
router.register(r'shoppingcartitems', ShoppingcartitemViewSet, basename='shoppingcartitem')
router.register(r'shoppingcarts', ShoppingcartViewSet)
router.register(r'categories', CategoryViewSet)

app_name = 'shopapi'
urlpatterns = [
    # Uri that conntects to api
    # search urlconfig MUST appear before 'productsbycategory'
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

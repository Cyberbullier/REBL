from django.urls import path, include
from . import views


app_name = 'shoppingcart'
urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.remove_from_cart,
         name='remove_from_cart'),
    path('full_remove/<int:product_id>/', views.full_remove,
         name='full_remove_from_cart')
]

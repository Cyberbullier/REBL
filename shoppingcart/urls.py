from django.urls import path, include
from . import views


app_name = 'shoppingcart'
urlpatterns = [
    # search urlconfig MUST appear before 'productsbycategory'
    path('add/<int:product_id>/', views.add_to_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail')
]

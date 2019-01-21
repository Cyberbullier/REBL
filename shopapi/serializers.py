from rest_framework import serializers
from shop.models import Apparel_products, Category
from shoppingcart.models import *


class ApparelProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apparel_products
        # only fields you allow client to access
        fields = ('id','category', 'name', 'description', 'slug',
                  'description', 'price', 'stock', 'product_available')

    read_only_fields = ['category']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # not sure about image field
        fields = ('id', 'name', 'description', 'image', 'cart_id', )


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('cart_id', 'date_made')


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ('product', 'shopping_cart', 'quantity', 'active')

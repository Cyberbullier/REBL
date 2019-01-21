from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404, HttpResponseNotAllowed
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from shoppingcart.views import add_to_cart,  remove_from_cart
from rest_framework import viewsets
from .serializers import (ApparelProductSerializer, Apparel_products,
Category, CategorySerializer, ShoppingCart, ShoppingCartSerializer,
ShoppingCartItem, ShoppingCartItemSerializer)


# Create your views here.


# ViewSets define the view behavior.
class ApparelproductsViewSet(viewsets.ModelViewSet):
    serializer_class = ApparelProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    #filter fields are exact and case sensitive
    # search fields are contains
    filter_fields = ('stock','product_available')
    search_fields = ('name','description')
    # possible parameters to order json
    ordering_fields = ('id', 'name')
    # how json is ordered if no ordering arguments are given
    ordering = ('stock', )
    #lookup_field = 'name'

    def get_queryset(self):
        stock = self.request.query_params.get('stock', None)
        if self.request.query_params.get('product_available') is False:
            availability = False
        else:
            availability = True
            # if product is in stock, doesnt necessarily mean available
            # for purchase
        if stock:
            if int(stock) >=1:
                return Apparel_products.objects.filter(product_available=availability,
                                                   stock__gte=int(stock))
            else:
                return Apparel_products.objects.filter(product_available=availability,
                                                   stock__lte=int(stock))
        else:
            return Apparel_products.objects.filter(product_available=availability)


    def retrieve(self, request, *args, **kwargs):
        if request.data == 'active':
            return Apparel_products.objects.filter(product_available=True)
        else:
            return HttpResponseNotAllowed('heyyyyyyy theres a bug')

    @action(detail=True)
    def deactivate(self, request, **kwwargs):
        """ability to deactivate product availability when api uri points
            to a unique id

        """
        product = self.get_object()
        product.product_available = False
        product.save()
        serializer = ApparelProductSerializer(product)
        return Response(serializer.data)

    @action(detail=False)
    def deactivate_all(self, request, *args, **kwargs):
        """ sets entire endpoint objects to unavailable"""
        products = Apparel_products.objects.filter(product_available=True)
        for x in products:
            x.product_available=False
            x.save()
        products = Apparel_products.objects.all()
        serializer = ApparelProductSerializer(products, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ShoppingcartViewSet(viewsets.ModelViewSet):

    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    #print(queryset)

class ShoppingcartitemViewSet(viewsets.ModelViewSet):

    serializer_class = ShoppingCartItemSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('product',)

    def get_queryset(self):
        product = self.request.query_params.get('product')
        if not product:
            print('gg bug')
            item = ShoppingCartItem.objects.all()
            serializer = ShoppingCartItemSerializer(item, many=True)
            return Response(serializer.data)
        else:
            print(product)
            return redirect('shop:shoppingcart:add_cart', product)

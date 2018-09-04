from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from shop.models import Season, Category, Apparel
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    """class based view for shop homepage"""
    template_name = 'shop/index.html'

def entire_product_listing(request, c_slug=None):
    """all products available"""
    products=None
    c_page=None
    if c_slug is None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Apparel



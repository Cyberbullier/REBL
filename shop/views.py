from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from shop.models import Season, Category, Apparel_products, Misc_products
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    """class based view for shop homepage"""

    template_name = 'shop/index.html'


def entire_product_listing(request, c_slug=None):
    """all products available"""
    c_page = None
    apparel = None
    if c_slug is None:
        apparel = Apparel_products.objects.all().filter(product_available=True)
    else:
        # gets query of all objects in Category with accepted slug
        # no objects exits, view returns 404 error page
        c_page=get_object_or_404(Category, slug=c_slug)
        apparel=Apparel_products.objects.all().filter(category=c_page,
                                                      product_available=True)

    context = {'category': c_page, 'apparel': apparel}
    return render(request, 'shop/category.html', context)

# get product description


def product_description(request, c_slug, product_slug):
    try:
        product = Apparel_products.objects.get(category__slug=c_slug,
                                               slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product':product})










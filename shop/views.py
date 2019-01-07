from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from shop.models import Season, Category, Apparel_products, Misc_products
from django.views.generic import TemplateView
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.


class HomeView(TemplateView):
    """class based view for shop homepage"""

    template_name = 'shop/index.html'


def entire_product_listing(request, c_slug=None):
    """all products available"""
    c_page = None
    apparel_list = None
    if c_slug is None:
        apparel_list = Apparel_products.objects.all().filter(product_available=True)
    else:
        # gets query of all objects in Category with accepted slug
        # no objects exits, view returns 404 error page
        c_page=get_object_or_404(Category, slug=c_slug)
        apparel_list=Apparel_products.objects.all().filter(category=c_page,
                                                           product_available=True)
    # implement page numbers and max products per page
    paginator = Paginator(apparel_list, 1)
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try:
        apparel_per_page = paginator.page(page)
    except (InvalidPage, EmptyPage):
        apparel_per_page = paginator.page(paginator.num_pages)

    context = {'category': c_page, 'apparel': apparel_per_page}
    return render(request, 'shop/category.html', context)

# get product description


def product_description(request, c_slug, product_slug):
    try:
        product = Apparel_products.objects.get(category__slug=c_slug,
                                               slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product':product})










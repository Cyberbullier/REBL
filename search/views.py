from django.shortcuts import render
from shop.models import Apparel_products
from django.db.models import Q
 # when deciding to send data back to server, consider...
 # use a URLPATH if you want to uniqeuely identify something
 # use QUERY PARAMETERS  if you want to manipulate how information is display,
 # such as a search, how many images to display a page per products

def search_result(request):
    products = None
    query = None
    # request.GET is python dictionary containing some paramters associated  with
    # the request object

    # maybe predefined query param?
    if "q" in request.GET:
        query = request.GET.get("q")
        # i..... means search is case insensitive
        # | is similar to python 'or', gets all objects that match at least 1
        # of the parameter
        products = Apparel_products.objects.all().filter(
                                                   Q(name__contains=query) |
                                                   Q(description__contains
                                                     =query), product_available=True
                                                        )
        print(products)
    context = {'products': products, 'query': query}
    return render(request, 'search/search_results.html', context)
# Create your views here.

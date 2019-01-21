from django.shortcuts import render, get_object_or_404
from .models import Order
# Create your views here.


def thank_you(request, unique_order_id):
    if unique_order_id is not None:
        customer_order = get_object_or_404(Order, id=unique_order_id)
        context = {'customer_order':customer_order}
        return render(request, 'thank_you.html', context)
    print('error here, customer order is was "None"')

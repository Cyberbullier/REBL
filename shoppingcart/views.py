from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Apparel_products
from .models import ShoppingCart, ShoppingCartItem
from order.models import Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
import stripe



# Create your views here.


def _cart_id(request):
    """user/anon cart"""
    cart = request.session.session_key
    if cart is None:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    # is this really needed?
    product = Apparel_products.objects.get(id=product_id)

    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    except ShoppingCart.DoesNotExist:
        # create new shopping cart object
        cart = ShoppingCart.objects.create(cart_id=_cart_id(request))
        # saves and creates new session for user
        cart.save()
# add or not add product to cart if cart
    try:
        cart_item = ShoppingCartItem.objects.get(product=product,
                                                 shopping_cart=cart)
        # if there are less of a specific item in a persons cart than
        # overall stock, then it is valid to add to cart
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
        # updates and saves current cart item count
    except ShoppingCartItem.DoesNotExist:
        cart_item = ShoppingCartItem.objects.create(product=product,
                                                   shopping_cart=cart,
                                                   quantity=1
                                                   )
        cart_item.save()
    # pass in name of url config namespace to reverse call the view function
    return redirect('shop:shoppingcart:cart_detail')

def remove_from_cart(request, product_id):
    cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Apparel_products, id=product_id)
    # queries for the item that is currently in sessions cart via product and shopping cart parameters

    cart_item = ShoppingCartItem.objects.get(product=product, shopping_cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('shop:shoppingcart:cart_detail')

def full_remove(request, product_id):
    """ fully removes an item from a unique cart"""
    cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Apparel_products, id=product_id)
    cart_item = ShoppingCartItem.objects.get(product=product,
                                             shopping_cart=cart)
    cart_item.delete()
    return redirect('shop:shoppingcart:cart_detail')

def cart_detail(request, cart_items=None):
    """organizes cart stock according to database, all view calls from this
    file should have this function call as its final call
    - split into helper functions
    """
    count = 0
    total = 0
    try:
        cart = ShoppingCart.objects.get(cart_id=_cart_id(request))
        # add filter if doesnt work
        # only use objects.get() if you know for sure there is only 1
        # object matching your arguments, otherwise use filter
        cart_items = ShoppingCartItem.objects.filter(shopping_cart=cart,
                                                     active=True)

        for x in cart_items:
            print(x.quantity)
            total += x.product.price*x.quantity
            count += x.quantity
    except ObjectDoesNotExist:
        print('you fucked up')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'REBL SHOP - new order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    # seperate into helper here
    if request.method == 'POST':
        try:
            print(request.POST)
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            # billing info
            billing_name = request.POST['stripeBillingName']
            billing_address1 = request.POST['stripeBillingAddressLine1']
            billing_postalcode =request.POST['stripeBillingAddressZip']
            billing_country = request.POST['stripeBillingAddressCountryCode']
            billing_city =request.POST['stripeBillingAddressCity']
            # shipping info
            shipping_name = request.POST['stripeShippingName']
            shipping_address1 = request.POST['stripeShippingAddressLine1']
            shipping_postalcode = request.POST['stripeShippingAddressZip']
            shipping_country = request.POST['stripeShippingAddressCountryCode']
            shipping_city = request.POST['stripeShippingAddressCity']
            customer = stripe.Customer.create(source=token, email=email)
            charge = stripe.Charge.create(amount=stripe_total, currency='cad',
                                          customer=customer.id, description=description
            )
            # create and save order into database
            try:
                order_details = Order.objects.create(token=token,
                                                     total=total,
                                                     email=email,
                                                     billing_name=billing_name,
                                                     billing_address1=billing_address1,
                                                     billing_postalcode=billing_postalcode,
                                                     billing_country=billing_country,
                                                     billing_city=billing_city,
                                                     shipping_name=shipping_name,
                                                     shipping_address1=shipping_address1,
                                                     shipping_postalcode=shipping_postalcode,
                                                     shipping_country=shipping_country,
                                                     shipping_city=shipping_city)
                order_details.save()
                for ordered_item in cart_items:
                    oi=OrderItem.objects.create(product=ordered_item.product.name,
                                                quantity=ordered_item.quantity,
                                                price=ordered_item.product.price,
                                                order=order_details)
                    oi.save()
                    # reduce current shop stock based on succesful orders
                    product = Apparel_products.objects.get(id=ordered_item.product.id)
                    product.stock = ordered_item.product.stock - ordered_item.quantity
                    product.save()
                    # deletes all relations this order_item, thus item doesnt
                    # appear in cart anymore
                    ordered_item.delete()
                    print('order has been create and updated proper2ly')
                    '''for now redirect to shop main page until i make
                    the thank you page '''
                    return redirect('shop:order:thanks', order_details.id)
            except ObjectDoesNotExist:
                pass
        except stripe.error.CardError as e:
            return False, e

    context = {'cart_items': cart_items, 'count': count, 'total': total,
               'stripe_total': stripe_total, 'description': description,
               'data_key': data_key
               }
    return render(request, 'shoppingcart/cart.html', context)

# no request param
def customer_email(order_id):
    transaction = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order__id=order_id)
    try:
        # sending the order email to the customer
        subject = "REBL FOLLOW UP EMAIL - ORDER #: {}".format(order_id)
        to = ['{}'.format(transaction.email)]
        # sandbox email
        from_email = 'postmaster@sandboxe5d1dc112fc34991a23b5db05172fa28.mailgun.org'
        order_info = {'transaction': transaction, 'order_items': order_items}
        email_content = get_template('email/email.html').render(order_info)
        msg = EmailMessage(subject, email_content, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
    except IOError as e:
        return e








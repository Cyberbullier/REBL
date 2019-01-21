from .models import ShoppingCartItem, ShoppingCart
from .views import _cart_id


def counter(request):
    """counter function for shopping cart
    """
    item_count = 0
    try:
        # retrieve a cart matching the current sessions id if it exists
        cart = ShoppingCart.objects.filter(cart_id=_cart_id(request))
        cart_items_recent_session = ShoppingCartItem.objects.\
            all().filter(shopping_cart=cart[:1])
        for item in cart_items_recent_session:
            item_count += item.quantity
    except ShoppingCart.DoesNotExist:
        pass
    context = {'item_count': item_count}
    return context


from django.db import models
from shop.models import Apparel_products

# Create your models here


class ShoppingCart(models.Model):
    """
     - implement shopping cart object with unique id per user
     - also, try to implement shopping cart object for a user with no account,
    closing/disconneccting with shop webpage will cause cart to empty.
    """
    # if blank is true, then user still has access to its cart?
    cart_id = models.CharField(max_length=250, blank=True)
    date_made = models.DateTimeField(auto_now_add=True)
    class Meta:
        """
        meta class in django is a container to store options, (ie, metadata),
        about the Model. From what I know, class Meta doesnt add any additional
        data to the Model, it just manipulates how the current data is
        accessed, permissions, etc, kinda of like quality of like changes
        """
        db_table = 'ShoppingCart'
        ordering = ['date_made']

    def __str__(self):
        """returns the carts unique id"""
        return self.cart_id

class ShoppingCartItem(models.Model):
    """
    items currently on sale at store that user put into cart
    - I think need to implement another class in shop app that encapsulates
    all products
    """
    # same product can be added to multiple users cart
    product = models.ForeignKey(on_delete=models.CASCADE, to=Apparel_products)
    shopping_cart = models.ForeignKey(ShoppingCart,
                                      on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # for when item count in users cart <= 0  via the user removing items
    # or the server being updated while item user wants to purchase is still
    # in car
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'ShoppingCartItem'

    def amount_due(self):
        """calculates total pricing of items in users cart pre tax/shipping"""
        return (self.product.price*self.quantity)

    def __str__(self):
        return self.product







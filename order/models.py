from django.db import models


class Order(models.Model):
    """
    token and email are blank so we canretrieve the data from stripe form
    """
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='CAD order total')
    email = models.EmailField(max_length=250, blank=True, verbose_name='email address')
    creation_date = models.DateTimeField(auto_now_add=True)
    billing_name = models.CharField(max_length=250, blank = True)
    billing_address1 = models.CharField(max_length=250, blank = True)
    billing_city = models.CharField(max_length=250, blank = True)
    billing_postalcode = models.CharField(max_length=250, blank = True)
    billing_country = models.CharField(max_length=250, blank = True)
    shipping_name = models.CharField(max_length=250, blank = True)
    shipping_address1 = models.CharField(max_length=250, blank = True)
    shipping_city = models.CharField(max_length=250, blank = True)
    shipping_postalcode = models.CharField(max_length=250, blank = True)
    shipping_country = models.CharField(max_length=250, blank = True)

    class Meta:
        # name of db table for this Model
        db_table = 'Order'
        # latest orders will appear at top row of database table
        ordering = ['-creation_date']

    def __str___(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="CAD price")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return (self.quantity * self.price)

    def __str__(self):
        return str(self.id)













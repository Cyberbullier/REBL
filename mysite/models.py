from django.db import models

class Season(models.Model):
    """
    unique season object  per clothing drop
    """
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='season', blank=True)
    season_available = models.BooleanField(default=True)

    class Meta:
        """
        meta-data per season
        """
        ordering = ('name',)
        verbose_name = 'season'
        verbose_name_plural = 'seasons'

    def __str__(self):
        return '{}'.format(self.name)


class Category(models.Model):
    """
    categories for products
    """
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    class Meta:
        """
        meta-data per category
        """
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def foreign_key_controller(self):
        """enable foreign key relationship with specific models."""


    def __str__(self):
        """

        :return: '{}'.format.(self.name)
        :rtype: str
        """
        return '{}'.format(self.name)


class Apparel(models.Model):
    """
    unique product per category per season
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    product_available = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_latest_update = models.DateTimeField(auto_now=True)


    class Meta:
        """
        meta-data for product
        """
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        """
        readable representation of class
        :return:
        :rtype: str
        """
        return '{}'.format(self.name )
# Create your models here.

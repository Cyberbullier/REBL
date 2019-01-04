from django.db import models
from django.urls import reverse

# Create your models here.

class Season(models.Model):
    """
    unique season object  per clothing drop
    """
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='season', blank=True, null=True)
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
    image = models.ImageField(blank=True, upload_to='category', null=True)


    class Meta:
        """
        meta-data per category
        """
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        """shortcut redirect url to all products in specified category"""
        return reverse('shop:productsbycategory', args=[self.slug])


    def __str__(self):
        """

        :return: '{}'.format.(self.name)
        :rtype: str
        """
        return '{}'.format(self.name)

# try season=models.ForeignKey(Season......, null=True) when creating objects in the shell

class Apparel_products(models.Model):
    """
    unique product per category per season
    """
    season = models.ForeignKey(Season, on_delete=models.CASCADE,
                               blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='product', blank=True, null=True)
    stock = models.IntegerField()
    product_available = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_latest_update = models.DateTimeField(auto_now=True)

    class Meta:
        """
        meta-data for product
        """
        ordering = ('name',)
        verbose_name = 'apparel'
        verbose_name_plural = 'apparel'

    def __str__(self):
        """
        readable representation of class
        :return:
        :rtype: str
        """
        return '{}'.format(self.name)


    def get_url(self):
        """
        returns specific products slug
        :return:
        """
        return reverse('shop:productdetail', args=[self.category.slug, self.slug])

class Misc_products(models.Model):
    """products not aassociated to Season"""

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
        verbose_name = 'misc product'
        verbose_name_plural = 'misc products'

    def __str__(self):
        """
        readable representation of class
        :return:
        :rtype: str
        """
        return '{}'.format(self.name)

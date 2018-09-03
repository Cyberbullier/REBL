from django.db import models

class Season(models.Model):
    """
    all garments of particular season
    """
    name = models.CharField(max_length=100, db_index=True)
    slug=models.SlugField(max_length=100, unique=True, db_index=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    # date of object creation
    updated_at = models.DateTimeField(auto_now=True)
    # last modified time stamp

    class Meta:
        ordering = ('name', )
        # watch yt vid what this tuple does again
        verbose_name='season'
        verbose_name_plural='seasons'






class Category(models.Model):
    """
    subsections per season
    """
    category = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='products')



# Create your models here.

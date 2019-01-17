"""custom module that contains functions that require request
  and available throughtout the  shop app"""

from .models import Category
from django.urls import reverse
from django.http import HttpResponseRedirect


def nav_bar_links(request) -> dict:
    """redirects user to category page"""
    links = Category.objects.all()
    navigation_bar_links = {'links': links}
    return navigation_bar_links

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse



# Create your views here.
def home(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    return render(request, 'mysite/index.html')

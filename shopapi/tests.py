
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from shop.models import Apparel_products
from .serializers import ApparelProductSerializer
import json

# ...

# Add this line at the top of the tests.py file
from django.contrib.auth.models import User


# update the BaseViewTest to this

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_newproduct(**kwargs):
        if kwargs['stock'] >= 1:
            Apparel_products.objects.create(kwargs)

    def login_a_user(self, username="", password=""):
        url = reverse(
            "auth-login",
            kwargs={
                "version": "v1"
            }
        )
        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type="application/json"
        )

    def setUp(self):
        # create a admin user
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )
        # add test data
        self.create_newproduct(kwargs={'season': None, 'category': 1,
                                       'name': 'LOL',
                                'slug': 'lol', 'price': 9, 'stock': 12})
        # self.create_song("simple song", "konshens")
        # self.create_song("love is wicked", "brick and lace")
        # self.create_song("jam rock", "damien marley")



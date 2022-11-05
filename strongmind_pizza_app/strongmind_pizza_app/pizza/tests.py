from django.test import TestCase
import pytest
from django.test.client import RequestFactory
from strongmind_pizza_app.pizza.models import Mastertoppings



class TestToppings(TestCase):

    @pytest.mark.django_db(True)
    def test_NewTopping(test):
        print(test)
        test_topping = "test_topping"
        assert len(Mastertoppings.objects.filter(mastertoppingname=test_topping.strip()).values()) == 0
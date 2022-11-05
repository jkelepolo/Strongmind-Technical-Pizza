from django.test import TestCase
import pytest
from django.test.client import RequestFactory
from .models import *

@pytest.mark.django_db(True)
def test_NewTopping():
    test_topping = "test_topping"
    assert len(Mastertoppings.objects.filter(mastertoppingname=test_topping.strip()).values()) == 0
from django.test import TestCase, Client
import pytest
from django.test.client import RequestFactory
from strongmind_pizza_app.pizza.models import Mastertoppings


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.login(username="UnitTest", password="strongmindtester")
    
    def test_PizzaBuild(self):
        response = self.client.get("/pizza/build/")
        assert response.status_code == 200

    def test_Toppings(self):
        response = self.client.get("/pizza/toppings/")
        assert response.status_code == 200

class TestToppings(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.login(username="UnitTest", password="strongmindtester")

    def test_NewTopping(self):
        response = self.client.post("/pizza/api/newtopping/", {"mastertoppingname":"test_topping"}, secure=True)
        assert response.status_code == 200
    
    def test_UpdateTopping(self):
        response = self.client.post("/pizza/api/updatetopping/", {"mastertoppingname":"test_topping", "mastertoppingid":0}, secure=True)
        assert response.status_code == 200
    
    def test_DeleteTopping(self):
        response = self.client.post("/pizza/api/deletetopping/", {"mastertoppingname":"test_topping", "mastertoppingid":0}, secure=True)
        assert response.status_code == 200

class TestPizzas(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.login(username="UnitTest", password="strongmindtester")

    def test_NewPizza(self):
        response = self.client.post("/pizza/api/newpizza/", {"masterpizzaname":"test_pizza"}, secure=True)
        assert response.status_code == 200
    
    def test_UpdatePizza(self):
        response = self.client.post("/pizza/api/updatepizza/", {"masterpizzaname":"test_pizza", "masterpizzaid":0}, secure=True)
        assert response.status_code == 200
    
    def test_DeletePizza(self):
        response = self.client.post("/pizza/api/deletepizza/", {"masterpizzaname":"test_pizza", "masterpizzaid":0}, secure=True)
        assert response.status_code == 200
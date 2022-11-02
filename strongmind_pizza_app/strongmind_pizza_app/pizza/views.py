from django.shortcuts import render
from .models import *

# Create your views here.


def vPizzaBuild(request):

    all_toppings = Mastertoppings.objects.all()
    all_pizzas = Masterpizzas.objects.all()
    pizza_components = Vucompletepizza.objects.all()

    context = {
        "pizzas": all_pizzas,
        "components":pizza_components,
        "toppings":all_toppings,
    }
    return render(request, "pizza/pizza.html", context)
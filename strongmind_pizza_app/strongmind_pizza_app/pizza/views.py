from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import *
from django.http import JsonResponse
import copy
import json

# VIEWS


@permission_required(perm=["pizza.masterpizzas.can_change_masterpizzas","pizza.masterpizzas.can_change_pizzacomponents"], login_url="/")
def vPizzaBuild(request):
    all_toppings = Mastertoppings.objects.all().values()
    all_pizzas = Masterpizzas.objects.all().values()
    pizza_components = Vucompletepizza.objects.all().values()

    complete_pizzas = []
    for pizza in all_pizzas:
        out_pizza = copy.deepcopy(pizza)
        out_pizza["toppings"] = []
        for component in pizza_components:
            if component["masterpizzaid"] == out_pizza["masterpizzaid"]:
                out_pizza["toppings"].append(component["mastertoppingid"])
        
        complete_pizzas.append(out_pizza)

    print(complete_pizzas)

    context = {
        "pizzas": complete_pizzas,
        "components":pizza_components,
        "toppings":all_toppings,
    }
    return render(request, "pizza/pizza.html", context)


# API Functions

@permission_required(perm=["pizza.masterpizzas.can_change_masterpizzas","pizza.masterpizzas.can_change_pizzacomponents"], login_url="/")
def apiUpdatePizza(request):
    if request.method == "POST":
        data = {key:val for key,val in request.POST.items()}

        Masterpizzas.objects.update(masterpizzaname=data["masterpizzaname"])
        
        data["checkbox_groups"] = json.loads(data["checkbox_groups"])
    
        if "Toppings" in data:
            components = Pizzacomponents.objects.filter(masterpizzaid=data["masterpizzaid"]).values()
            saved_toppings = [str(component["mastertoppingid"]) for component in components]

            for component in components:
                print(component["mastertoppingid"], data["checkbox_groups"]["Toppings"])
                if str(component["mastertoppingid"]) not in data["checkbox_groups"]["Toppings"]:
                    Pizzacomponents.objects.filter(pizzacomponentid=component["pizzacomponentid"]).delete()
            
            for topping in data["checkbox_groups"]["Toppings"]:
                if topping not in saved_toppings:
                    new_component = Pizzacomponents(masterpizzaid=data["masterpizzaid"], mastertoppingid=topping)
                    new_component.save()
        else:
            Pizzacomponents.objects.filter(masterpizzaid=data["masterpizzaid"]).delete()

    return JsonResponse({}, status=200)

@permission_required(perm=["pizza.masterpizzas.can_change_masterpizzas","pizza.masterpizzas.can_change_pizzacomponents"], login_url="/")
def apiDeletePizza(request):
    if request.method == "POST":
        data = {key:val for key,val in request.POST.items()}

        Masterpizzas.objects.filter(masterpizzaid=data["masterpizzaid"]).delete()
        Pizzacomponents.objects.filter(masterpizzaid=data["masterpizzaid"]).delete()
    return JsonResponse({"refresh":""}, status=200)

@permission_required(perm=["pizza.masterpizzas.can_change_masterpizzas","pizza.masterpizzas.can_change_pizzacomponents"], login_url="/")
def apiNewPizza(request):
    if request.method == "POST":
        NewPizza = Masterpizzas(masterpizzaname="New Pizza")
        NewPizza.save()
    return JsonResponse({"refresh":""}, status=200)
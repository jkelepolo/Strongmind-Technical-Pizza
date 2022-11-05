from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import *
from django.http import JsonResponse
import copy
import json

# VIEWS


@permission_required(perm=["pizza.change_masterpizzas","pizza.change_pizzacomponents"], login_url="/")
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
        "pizzas": complete_pizzas[::-1],
        "components":pizza_components,
        "toppings":all_toppings[::-1],
    }
    return render(request, "pizza/pizza.html", context)

@permission_required(perm=["pizza.change_mastertoppings"], login_url="/")
def vToppings(request):
    all_toppings = Mastertoppings.objects.all().values()

    context = {
        "toppings": all_toppings[::-1],
    }
    return render(request, "pizza/toppings.html", context)

# API Functions

# Pizza API
@permission_required(perm=["pizza.change_masterpizzas","pizza.change_pizzacomponents"], login_url="/")
def apiUpdatePizza(request):
    if request.method == "POST":
        data = {key:val for key,val in request.POST.items()}
        
        
        if "checkbox_groups" in data:
            data["checkbox_groups"] = json.loads(data["checkbox_groups"])
        
        print(data)

        if "masterpizzaname" in data:
            if data["masterpizzaname"].strip() == "":
                return JsonResponse({"toast":["danger", "Name cannot be empty!"]}, status=200)
            for pizza in Masterpizzas.objects.all().values():
                if data["masterpizzaname"].lower().strip() == pizza["masterpizzaname"].lower().strip() and str(data["masterpizzaid"]) != str(pizza["masterpizzaid"]):
                    return JsonResponse({"toast":["danger", "No duplicate names allowed!"]}, status=200)

            Masterpizzas.objects.filter(masterpizzaid=data["masterpizzaid"]).update(masterpizzaname=data["masterpizzaname"].strip())


    
        if "Toppings" in data:
            components = Pizzacomponents.objects.filter(masterpizzaid=data["masterpizzaid"]).values()
            saved_toppings = [str(component["mastertoppingid"]) for component in copy.deepcopy(components)]

            
            for component in components:
                if str(component["mastertoppingid"]) not in data["checkbox_groups"]["Toppings"]:
                    print(component["mastertoppingid"], data["checkbox_groups"]["Toppings"])

                    Pizzacomponents.objects.filter(pizzacomponentid=component["pizzacomponentid"]).delete()
            
            for topping in data["checkbox_groups"]["Toppings"]:
                if topping not in saved_toppings:
                    new_component = Pizzacomponents(masterpizzaid=data["masterpizzaid"], mastertoppingid=topping)
                    new_component.save()
        else:
            Pizzacomponents.objects.filter(masterpizzaid=data["masterpizzaid"]).delete()

    return JsonResponse({}, status=200)

@permission_required(perm=["pizza.change_masterpizzas","pizza.change_pizzacomponents"], login_url="/")
def apiDeletePizza(request):
    if request.method == "POST":
        data = {key:val for key,val in request.POST.items()}

        Masterpizzas.objects.filter(masterpizzaid=data["masterpizzaid"]).delete()
        Pizzacomponents.objects.filter(masterpizzaid=data["masterpizzaid"]).delete()
    return JsonResponse({"refresh":""}, status=200)

@permission_required(perm=["pizza.change_masterpizzas","pizza.change_pizzacomponents"], login_url="/")
def apiNewPizza(request):
    if request.method == "POST":
        data = {key:val for key,val in request.POST.items()}

        print(data)
        if "masterpizzaname" in data:
            if data["masterpizzaname"].strip() == "":
                return JsonResponse({"toast":["danger", "Name cannot be empty!"]}, status=200)
            for pizza in Masterpizzas.objects.all().values():
                if data["masterpizzaname"].lower().strip() == pizza["masterpizzaname"].lower().strip():
                    return JsonResponse({"toast":["danger", "No duplicate names allowed!"]}, status=200)


            NewPizza = Masterpizzas(masterpizzaname=data["masterpizzaname"].strip())
            NewPizza.save()

    return JsonResponse({"refresh":""}, status=200)


# Topping API

@permission_required(perm=["pizza.change_mastertoppings"], login_url="/")
def apiUpdateTopping(request):

    if request.method == "POST":
        data = {key:val for key,val in request.POST.items()}

        if data["mastertoppingname"].strip() == "":
            return JsonResponse({"toast":["danger", "Name cannot be empty!"]}, status=200)

        for topping in Mastertoppings.objects.all().values():
            if data["mastertoppingname"].lower().strip() == topping["mastertoppingname"].lower().strip() and str(data["mastertoppingid"]) != str(topping["mastertoppingid"]):
                return JsonResponse({"toast":["danger", "No duplicate names allowed!"]}, status=200)

    Mastertoppings.objects.filter(mastertoppingid=data["mastertoppingid"]).update(mastertoppingname=data["mastertoppingname"].strip())

    return JsonResponse({}, status=200)

@permission_required(perm=["pizza.change_mastertoppings"], login_url="/")
def apiNewTopping(request):

    if request.method == "POST":
        data = {key:val for key,val in request.POST.items()}

        if data["mastertoppingname"].strip() == "":
            return JsonResponse({"toast":["danger", "Name cannot be empty!"]}, status=200)
    
        for topping in Mastertoppings.objects.all().values():
            if data["mastertoppingname"].lower().strip() == topping["mastertoppingname"].lower().strip():
                return JsonResponse({"toast":["danger", "No duplicate names allowed!"]}, status=200)

        NewTopping = Mastertoppings(mastertoppingname=data["mastertoppingname"].strip())
        NewTopping.save()

    return JsonResponse({"refresh":""}, status=200)

@permission_required(perm=["pizza.change_mastertoppings"], login_url="/")
def apiDeleteTopping(request):

    if request.method == "POST":
        data = {key:val for key,val in request.POST.items()}
        Mastertoppings.objects.filter(mastertoppingid=data["mastertoppingid"]).delete()
        Pizzacomponents.objects.filter(masterpizzaid=data["mastertoppingid"]).delete()

    return JsonResponse({"refresh":""}, status=200)
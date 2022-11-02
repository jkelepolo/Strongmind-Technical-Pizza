from django.db import models

# TABLES

class Masterpizzas(models.Model):
    masterpizzaid = models.AutoField(unique=True, primary_key=True)
    masterpizzaname = models.TextField()

    class Meta:
        managed = False
        db_table = 'MasterPizzas'


class Mastertoppings(models.Model):
    mastertoppingid = models.AutoField(unique=True, primary_key=True)
    mastertoppingname = models.TextField()

    class Meta:
        managed = False
        db_table = 'MasterToppings'

class Pizzacomponents(models.Model):
    pizzacomponentid = models.AutoField(unique=True, primary_key=True)
    masterpizzaid = models.IntegerField()
    mastertoppingid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PizzaComponents'

# VIEWS

class Vucompletepizza(models.Model):
    pizzacomponentid = models.IntegerField(primary_key=True)
    mastertoppingid = models.IntegerField(blank=True, null=True)
    masterpizzaid = models.IntegerField(blank=True, null=True)
    masterpizzaname = models.TextField(blank=True, null=True)
    mastertoppingname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vuCompletePizza'
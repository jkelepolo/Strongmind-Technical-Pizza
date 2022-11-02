from django.db import models

# Create your models here.

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
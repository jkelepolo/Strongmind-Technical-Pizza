# Generated by Django 4.0.8 on 2022-11-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Masterpizzas',
            fields=[
                ('masterpizzaid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('masterpizzaname', models.TextField()),
            ],
            options={
                'db_table': 'MasterPizzas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mastertoppings',
            fields=[
                ('mastertoppingid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('mastertoppingname', models.TextField()),
            ],
            options={
                'db_table': 'MasterToppings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pizzacomponents',
            fields=[
                ('pizzacomponentid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('masterpizzaid', models.IntegerField()),
                ('mastertoppingid', models.IntegerField()),
            ],
            options={
                'db_table': 'PizzaComponents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vucompletepizza',
            fields=[
                ('pizzacomponentid', models.IntegerField(primary_key=True, serialize=False)),
                ('mastertoppingid', models.IntegerField(blank=True, null=True)),
                ('masterpizzaid', models.IntegerField(blank=True, null=True)),
                ('masterpizzaname', models.TextField(blank=True, null=True)),
                ('mastertoppingname', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vuCompletePizza',
                'managed': False,
            },
        ),
    ]

# Strongmind Pizza App

Strongmind Pizza App - Technical interview

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Building Locally

- Setting up an anaconda environment:

        $ conda create -n strongmind python=3.10.6
        $ conda activate strongmind

- Setting up python venv:

        $ python -m venv [directory]
        $ [directory]\Scripts\activate.bat

- Using your anaconda environment or python venv:

        $ cd ..\strongmind_pizza_app\
        $ pip install -r requirements/local.txt


### Setting Up Your Users

-   To login as a **Pizza Chef** use these credentials under the sign-in page:

        User: PizzaChef
        Password: strongmindchef

-   To login as a **Pizza Store Owner** use these credentials under the sign-in page:

        User: StoreOwner
        Password: strongmindown

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

-   As a **superuser** you can manage accounts and permissions under the admin panel:

        appdomain.com/admin

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


#### Running unit tests

    $ pytest


## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

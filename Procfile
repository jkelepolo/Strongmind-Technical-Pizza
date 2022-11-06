release: python strongmind_pizza_app/manage.py migrate
web: gunicorn --chdir strongmind_pizza_app config.wsgi:application

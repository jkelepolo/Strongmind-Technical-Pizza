from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PizzaConfig(AppConfig):
    name = 'strongmind_pizza_app.pizza'
    verbose_name = _("Pizza")

    def ready(self):
        try:
            import strongmind_pizza_app.pizza.signals  # noqa F401
        except ImportError:
            pass
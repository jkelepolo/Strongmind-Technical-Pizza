from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from .views import *

app_name = "pizza"
urlpatterns = [
   path("build/", TemplateView.as_view(template_name="pizza/pizza.html"), name="pizza"),
   path("toppings/", TemplateView.as_view(template_name="pizza/toppings.html"), name="pizza"),
]
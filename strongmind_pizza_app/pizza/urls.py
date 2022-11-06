from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from .views import *

app_name = "pizza"
urlpatterns = [
   # Pages
   path("build/", vPizzaBuild, name="pizza"),
   path("toppings/", vToppings, name="pizza"),

   #API Calls

   # Pizza API
   path("api/updatepizza/", apiUpdatePizza, name="updatepizza"),
   path("api/deletepizza/", apiDeletePizza, name="deleteizza"),
   path("api/newpizza/", apiNewPizza, name="newpizza"),

   # Topping API
   path("api/updatetopping/", apiUpdateTopping, name="updatetopping"),
   path("api/deletetopping/", apiDeleteTopping, name="deletetopping"),
   path("api/newtopping/", apiNewTopping, name="newtopping"),
]

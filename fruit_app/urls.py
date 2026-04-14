from django.urls import path

from .views import send_fruits, send_fruits_template

urlpatterns = [path("", send_fruits), path("list/", send_fruits_template)]

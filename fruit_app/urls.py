from django.urls import path

from .views import fruit_info, send_fruits, send_fruits_template

urlpatterns = [
    path("", send_fruits),
    path("list/", send_fruits_template),
    path("list/info", fruit_info),
]

from django.urls import path

from fruit_app.views import send_fruits

urlpatterns = [
    path("", send_fruits),
]
